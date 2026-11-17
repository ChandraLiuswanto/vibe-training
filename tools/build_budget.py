"""Rebuild budgetting.xlsx: Sheet1 from ROWS, sheet "VPS Providers" from OFFERS.

Specs: docs/superpowers/specs/2026-11-16-training-budget-design.md (Sheet1),
       docs/superpowers/specs/2026-11-17-vps-providers-pricing-design.md (sheet "VPS Providers").
Sheet1 prices checked 2026-11-16: digitalocean.com/pricing/droplets, api.vultr.com/v2/plans, cfdomainpricing.com (Cloudflare Registrar at cost).
VPS Providers: each row carries its own check date; sources in docs/reviews/2026-11-17-vps-price-evidence.md.
"""
from dataclasses import dataclass
from pathlib import Path

import openpyxl
from openpyxl.styles import Font

XLSX = Path(__file__).resolve().parent.parent / "budgetting.xlsx"
TAX = 0.11

# (item, plan, period, quantity, price USD, note)
ROWS = [
    ("Codex", "Pro 200", "Monthly", 1, 200,
     "Shared via 9router for opencode (agentic coding) + in-app chatbot"),
    ("VPS - 9router", "DigitalOcean Basic 1 vCPU / 2 GB / 50 GB SSD, Singapore (SGP1)", "Monthly", 1, 12,
     "Separate from deploy box so a broken deploy can't stop the agents; hourly billing, monthly cap"),
    ("VPS - Day 5 deploy (shared, subdomain per team)",
     "Vultr Cloud Compute 16 vCPU / 64 GB / 1.28 TB SSD, Singapore (vc2-16c-64gb)", "Monthly", 1, 320,
     "Recommended pick; see sheet 'VPS Providers' for alternatives. Hourly billing, monthly cap"),
    ("Domain", ".com via Cloudflare Registrar (at-cost) for teamN.<domain>", "Yearly", 1, 10.46,
     "Free fallback: teamN.<ip>.sslip.io"),
    ("GitHub", "Free", "-", 1, 0, "Participant repos + checkpoint repo"),
    ("opencode", "Open source", "-", 1, 0, "Coding agent"),
    ("Container tool (laptops)", "Podman Desktop (free)", "-", 1, 0,
     "Docker Desktop is not free for companies >250 staff / >$10M revenue"),
    ("TLS certificates", "Let's Encrypt", "-", 1, 0, "HTTPS for team subdomains"),
    ("Market data", "yfinance", "-", 1, 0, "Yahoo Finance data, no key"),
    ("Demo video", "HyperFrames (open source)", "-", 1, 0, "Final showcase"),
]

NOTE = ("Optional, not in total: Docker Desktop Business ~$24/user/mo, "
        "only if OCBC IT requires Docker Desktop instead of Podman.")
ASSUMPTION = ("Assumes trainer prep + Day 3-5 delivery fit within 1 billing month; "
              "domain = first year. If prep spans 2 months, set Quantity = 2 on the Monthly rows.")


# 1 USD in each currency. ECB via https://api.frankfurter.app/latest?from=USD&to=EUR,IDR,SGD
PER_USD = {"USD": 1.0, "EUR": 0.90794, "IDR": 18259, "SGD": 1.2888}
RATES_DATE = "2026-11-16"

PROVIDER_HEADER = ["Provider", "Product / plan", "vCPU", "RAM (GB)", "Disk", "Location", "In Indonesia?",
                   "Price (website)", "Price USD / month", "Billing", "Fits 16/64?", "Price status", "Checked",
                   "Notes", "Link"]


@dataclass(frozen=True)
class Offer:
    """One plan in one location, with the price the provider's own site shows for exactly that."""
    provider: str
    plan: str             # as the website names it
    vcpu: int | None      # None when the plan list could not be read
    ram_gb: int | None
    disk: str
    location: str         # one place; "Not stated" when the site does not say
    in_indonesia: bool | None  # None when the site does not say where the server is
    price_text: str       # as shown on the site
    currency: str         # key of PER_USD
    amount: float | None  # monthly, before tax, in `currency`; None when not confirmed
    billing: str
    fits: str             # "Yes", "No (reason)", or "Not confirmed (reason)" when the plan list could not be read
    status: str           # "Confirmed" or "Not confirmed (reason)"
    checked: str          # YYYY-MM-DD the price was read
    notes: str
    link: str             # page the price came from


HOURLY_CAP = "Hourly, capped at the monthly price"
HOURS = 730  # hours in a month, for clouds that publish an hourly price only
ON_DEMAND = "Hourly, on-demand, no monthly cap"
SUBSCRIPTION = "Monthly subscription; or pay-as-you-go by the hour"
CONSOLE_ONLY = "Not confirmed (prices load only inside the provider's console; the public page shows none)"
# Day 5 deploy VPS candidates, target 16 vCPU / 64 GB. Evidence per row: docs/reviews/2026-11-17-vps-price-evidence.md
OFFERS = [
    Offer("Vultr", "Cloud Compute Regular vc2-16c-64gb", 16, 64, "1280 GB SSD", "Singapore", False,
          "$320/mo ($0.438/hr)", "USD", 320, HOURLY_CAP, "Yes", "Confirmed", "2026-11-17",
          "Current pick in the main sheet. Shared vCPU. Same price in every Vultr region; Vultr has no Indonesian region.",
          "https://www.vultr.com/pricing/"),
    Offer("Vultr", "Optimized Cloud General Purpose voc-g-16c-64gb-320s-amd", 16, 64, "320 GB", "Singapore", False,
          "$480/mo ($0.658/hr)", "USD", 480, HOURLY_CAP, "Yes", "Confirmed", "2026-11-17",
          "Dedicated vCPU: steadier under 30 parallel builds. Same price in every Vultr region.",
          "https://www.vultr.com/pricing/"),
    Offer("Hetzner", "CCX43 (dedicated vCPU)", 16, 64, "360 GB NVMe", "Singapore", False,
          "EUR 341.49/mo excl. VAT", "EUR", 341.49, HOURLY_CAP, "Yes", "Confirmed", "2026-11-17",
          "Singapore costs 45% more than Helsinki. Price includes IPv4.",
          "https://www.hetzner.com/cloud/general-purpose"),
    Offer("Hetzner", "CCX43 (dedicated vCPU)", 16, 64, "360 GB NVMe", "Helsinki", False,
          "EUR 234.99/mo excl. VAT", "EUR", 234.99, HOURLY_CAP, "Yes", "Confirmed", "2026-11-17",
          "Reference only: Hetzner's cheapest region, far from Indonesia (high latency). "
          "This is the price the old sheet showed under 'Singapore'.",
          "https://www.hetzner.com/cloud/general-purpose"),
    Offer("Hetzner", "CPX62 (shared vCPU)", 16, 32, "640 GB NVMe", "Singapore", False,
          "EUR 172.49/mo excl. VAT", "EUR", 172.49, HOURLY_CAP, "No (32 GB RAM)", "Confirmed", "2026-11-17",
          "Listed for reference only. Helsinki price is EUR 110.99.",
          "https://www.hetzner.com/cloud/regular-performance"),
    Offer("Akamai Linode", "Shared CPU Linode 64GB (g6-standard-16)", 16, 64, "1280 GB SSD", "Jakarta", True,
          "$460.80/mo ($0.691/hr)", "USD", 460.80, HOURLY_CAP, "Yes", "Confirmed", "2026-11-17",
          "Jakarta region (id-cgk) costs 20% more than Linode's standard regions.",
          "https://www.linode.com/pricing/"),
    Offer("Akamai Linode", "Shared CPU Linode 64GB (g6-standard-16)", 16, 64, "1280 GB SSD", "Singapore", False,
          "$384/mo ($0.576/hr)", "USD", 384, HOURLY_CAP, "Yes", "Confirmed", "2026-11-17",
          "Standard price; Singapore has no regional surcharge.",
          "https://www.linode.com/pricing/"),
    Offer("AWS Lightsail", "Linux bundle 64 GB / 16 vCPU, public IPv4", 16, 64, "1280 GB SSD", "Jakarta", True,
          "$384 USD/mo", "USD", 384, HOURLY_CAP, "Yes", "Confirmed", "2026-11-17",
          "CPU type not stated. Same bundle price in every Region, but Jakarta includes half the data transfer (4 TB instead of 8 TB).",
          "https://aws.amazon.com/lightsail/pricing/"),
    Offer("AWS Lightsail", "Linux bundle 64 GB / 16 vCPU, public IPv4", 16, 64, "1280 GB SSD", "Singapore", False,
          "$384 USD/mo", "USD", 384, HOURLY_CAP, "Yes", "Confirmed", "2026-11-17",
          "CPU type not stated. Same bundle price in every Region; 8 TB data transfer included.",
          "https://aws.amazon.com/lightsail/pricing/"),
    Offer("UpCloud", "Premium 64 GB / 16 cores", 16, 64, "300 GB MaxIOPS", "Singapore", False,
          "EUR 384/mo (Global price)", "EUR", 384, "Hourly, capped at 28 days per month", "Yes", "Confirmed", "2026-11-17",
          "CPU type not stated. 'Global price' applies to every UpCloud data centre, Singapore (SG-SIN1) included. 99.999% SLA. "
          "A Cloud Native 64 GB / 16 cores plan is EUR 270/mo with storage billed separately.",
          "https://upcloud.com/pricing/"),
    Offer("DigitalOcean", "General Purpose Droplet g-16vcpu-64gb (dedicated vCPU)", 16, 64, "200 GB SSD", "Singapore", False,
          "$504.00/mo ($0.75/hr)", "USD", 504, HOURLY_CAP, "Yes", "Confirmed", "2026-11-17",
          "The pricing page shows one price, with no per-region difference. Same provider as the 9router VPS.",
          "https://www.digitalocean.com/pricing/droplets"),
    Offer("Contabo", "Cloud VPS 16", 16, 64, "500 GB SSD or 250 GB NVMe", "Singapore", False,
          "EUR 37.00/mo + EUR 20.75/mo Asia (Singapore) location fee", "EUR", 57.75,
          "Monthly, prepaid; 1-month contract", "Yes", "Confirmed", "2026-11-17",
          "OUT OF STOCK in Singapore when checked. Price includes the Singapore location fee, which the old sheet left out. No setup fee. The order page does not state VAT. "
          "12-month price EUR 31.45, 24-month EUR 29.60, "
          "plus the same location fee. Very cheap, shared hosts: the old sheet flagged it as risky for a live class.",
          "https://contabo.com/en/vps/cloud-vps-core-16"),
    Offer("Contabo", "Cloud VPS 16", 16, 64, "500 GB SSD or 250 GB NVMe", "European Union", False,
          "EUR 37.00/mo", "EUR", 37.00, "Monthly, prepaid; 1-month contract", "Yes", "Confirmed", "2026-11-17",
          "Reference only: Contabo's cheapest region (no location fee), far from Indonesia. CPU type not stated. No setup fee. The order page does not state VAT.",
          "https://contabo.com/en/vps/cloud-vps-core-16"),
    Offer("OVHcloud", "VPS-4 (largest VPS)", 8, 24, "200 GB NVMe", "Singapore", False,
          "From S$30 ex. GST/month", "SGD", None, "Monthly", "No (max 8 vCPU / 24 GB)",
          "Not confirmed (the Singapore site shows a 'from' price without naming the data centre or the commitment)",
          "2026-11-17", "Listed for reference only.",
          "https://www.ovhcloud.com/en-sg/vps/"),
    Offer("Biznet Gio", "NEO Lite LL 16.16 (largest NEO Lite)", 16, 16, "60 GB SSD", "Indonesia", True,
          "Rp998.000/bulan (promo Rp499.000)", "IDR", 998000, "Monthly", "No (16 GB RAM)", "Confirmed", "2026-11-17",
          "Regular price used; Rp499.000 is a new-customer promo. CPU type not stated. The page says 'Data Center di Indonesia' without naming "
          "the city, and does not say whether PPN is included. Listed for reference only.",
          "https://www.biznetgio.com/product/neo-lite"),
    # Indonesian providers
    Offer("Rumahweb", "VPS Indonesia X4L (Linux)", 16, 64, "1,200 GB SSD", "Bogor", True,
          "Rp3.750.000/bulan", "IDR", 3750000, "Monthly", "Yes", "Confirmed", "2026-11-17",
          "Zone A, TechnoVillage Bogor (Tier 3). Regular price used; the page advertised 50% off Linux plans from Paket S up "
          "(promo terms not read). CPU type not stated. Unmetered bandwidth. The page does not say whether PPN is included.",
          "https://www.rumahweb.com/vps-indonesia/"),
    Offer("Rumahweb", "VPS Indonesia X4L (Linux)", 16, 64, "1,200 GB SSD", "Bekasi", True,
          "Rp3.760.000/bulan", "IDR", 3760000, "Monthly", "Yes", "Confirmed", "2026-11-17",
          "Zone B, DCI Indonesia Bekasi (Tier 4). Regular price used; the page advertised 50% off Linux plans from Paket S up "
          "(promo terms not read). CPU type not stated. Unmetered bandwidth. The page does not say whether PPN is included.",
          "https://www.rumahweb.com/vps-indonesia/"),
    Offer("Qwords", "Cloud VPS KVM SC64", 16, 64, "1,280 GB SSD (RAID 10)", "Jakarta", True,
          "Rp6.850.000/bulan (Rp6.750.000/bulan on a yearly cycle)", "IDR", 6850000, "Monthly; also 3, 6 or 12 months",
          "Yes", "Confirmed", "2026-11-17",
          "The page preselects the yearly cycle, so it shows Rp6.750.000; one month costs Rp6.850.000. No setup fee. "
          "Shared ('equal share') CPU. The page does not say whether PPN is included.",
          "https://www.qwords.com/vps-indonesia/cloud-vps-kvm-ssd/"),
    Offer("DomaiNesia", "Cloud VPS Turbo 64GB", 16, 64, "960 GB SSD NVMe", "Jakarta", True,
          "Rp9.600.000/bulan (first cycle Rp4.800.000/bulan, Diskon 50%)", "IDR", 9600000, "Monthly; also 3, 6 or 12 months",
          "Yes", "Confirmed", "2026-11-17",
          "Regular price used: the page gives it as the renewal price ('Harga perpanjangan'). CPU type not stated. New orders get 50% off with promo code CLOUDHANDAL, on any cycle from 1 month. "
          "The cart adds PPN on top, so this is the price before tax.",
          "https://www.domainesia.com/cloud-vps/"),
    Offer("Jagoan Hosting", "VPS NextGen MULTIVERSE (custom) 16 core / 96 GB", 16, 96, "1,000 GB", "Not stated", None,
          "Rp4.360.000/bln (16 x Rp30.000 + 96 x Rp30.000 + 1,000 x Rp1.000)", "IDR", 4360000, "Monthly",
          "No (16 cores requires at least 96 GB RAM and 1,000 GB disk)", "Confirmed", "2026-11-17",
          "Built from the configurator's unit prices: Rp30.000 per core, Rp30.000 per GB RAM, Rp1.000 per GB disk. "
          "Larger than the target, so it would work, at a higher price. CPU type not stated. Price excludes PPN 11%. The page calls the product "
          "'VPS Indonesia' without naming the data centre. Fixed plans stop at 6 core / 6 GB.",
          "https://www.jagoanhosting.com/vps-indonesia/"),
    Offer("CloudKilat", "Kilat VPS XL (largest)", 32, 32, "320 GB SSD", "Indonesia", True,
          "Rp2.880.000/bulan", "IDR", 2880000, "Monthly", "No (max 32 GB RAM)", "Confirmed", "2026-11-17",
          "Listed for reference only. CPU type not stated. NEX Data Center, Tier 3. Paket L is 16 vCPU / 16 GB at Rp1.440.000. "
          "The page does not say whether PPN is included.",
          "https://www.cloudkilat.com/id/kilat-vps/"),
    Offer("Hostinger", "KVM 8 (largest)", 8, 32, "400 GB NVMe", "Jakarta", True,
          "Rp853.900/bln on renewal (Rp426.900/bln for the first 24 months)", "IDR", 853900,
          "24-month term, prepaid (Rp10.245.600 up front)", "No (max 8 vCPU / 32 GB)", "Confirmed", "2026-11-17",
          "Listed for reference only. The page says its VPS plans get dedicated CPU, RAM and storage. Renewal price used; the first 24-month term costs half. Prices exclude PPN. "
          "Jakarta is one of the 10 data centres the page lists.",
          "https://www.hostinger.com/id/hosting-vps"),
    Offer("Biznet Gio", "NEO Lite Pro LL.24.12 (largest NEO Lite Pro)", 12, 24, "100 GB NVMe", "Indonesia", True,
          "Rp2.849.000/bulan (promo Rp2.299.000)", "IDR", 2849000, "Monthly", "No (max 12 vCPU / 24 GB)", "Confirmed",
          "2026-11-17",
          "Listed for reference only. Struck-through price used as the regular price; Rp2.299.000 is a promo. Dedicated vCPU "
          "and RAM. The page says 'Data Center Lokal' without naming the city, and does not say whether PPN is included.",
          "https://www.biznetgio.com/product/neo-lite-pro"),
    Offer("Biznet Gio", "NEO Virtual Compute", None, None, "-", "Not stated", None,
          "Not found", "IDR", None, "-", "Not confirmed (product not found on the site)",
          "Not confirmed (biznetgio.com has no NEO Virtual Compute page and its product list does not show it)",
          "2026-11-17", "The larger Biznet line the old plan expected. Ask Biznet Gio sales whether it is still sold.",
          "https://www.biznetgio.com/product"),
    Offer("IDCloudHost", "Cloud VPS", None, None, "-", "Not stated", None,
          "Not read", "IDR", None, "-", "Not confirmed (plan list could not be read)", "Not confirmed (the site blocks automated reading; open the link in a browser)", "2026-11-17",
          "Indonesian provider. Sizes and prices need a manual look.",
          "https://idcloudhost.com/cloud-vps/"),
    Offer("Dewaweb", "Cloud VPS", None, None, "-", "Not stated", None,
          "Not read", "IDR", None, "-", "Not confirmed (plan list could not be read)", "Not confirmed (the site blocks automated reading; open the link in a browser)", "2026-11-17",
          "Indonesian provider. Sizes and prices need a manual look.",
          "https://www.dewaweb.com/cloud-vps"),
    Offer("Niagahoster", "Cloud VPS", None, None, "-", "Not stated", None,
          "Not read", "IDR", None, "-", "Not confirmed (plan list could not be read)",
          "Not confirmed (site redirects to Hostinger)", "2026-11-17",
          "niagahoster.co.id now forwards to hostinger.com/id. See the Hostinger row.",
          "https://www.niagahoster.co.id/"),
    # Global clouds with a Jakarta region. Instance price only: disk and bandwidth are billed separately.
    Offer("Alibaba Cloud", "ECS ecs.u2a-c1m4.4xlarge (general-purpose, AMD)", 16, 64, "Not included", "Jakarta", True,
          "$323.50 for 1 month ($0.6628/hr pay-as-you-go)", "USD", 323.50, SUBSCRIPTION, "Yes", "Confirmed", "2026-11-17",
          "Cheapest general-purpose 16 vCPU / 64 GB type in Jakarta by monthly price. CPU type not stated. Pay-as-you-go for a full month would be "
          "$483.84. Disk and bandwidth are extra. Next: ecs.g8a.4xlarge at $359.44.",
          "https://www.alibabacloud.com/product/ecs-pricing-list/en"),
    Offer("Alibaba Cloud", "ECS ecs.u2a-c1m4.4xlarge (general-purpose, AMD)", 16, 64, "Not included", "Singapore", False,
          "$365.00 for 1 month ($0.6628/hr pay-as-you-go)", "USD", 365.00, SUBSCRIPTION, "Yes", "Confirmed", "2026-11-17",
          "Same type as the Jakarta row; the monthly price is higher in Singapore. CPU type not stated. Disk and bandwidth are extra.",
          "https://www.alibabacloud.com/product/ecs-pricing-list/en"),
    Offer("Huawei Cloud", "ECS x2.16u.64g (General Computing, X2)", 16, 64, "Not included", "Jakarta", True,
          "$359.93 for 1 month ($0.6848/hr pay-per-use)", "USD", 359.93, SUBSCRIPTION, "Yes", "Confirmed", "2026-11-17",
          "Cheapest 16 vCPU / 64 GB x86 type in AP-Jakarta (tied with x1 and x2e). CPU type not stated. Pay-per-use for a full month would be "
          "$499.90. Disk and bandwidth are priced separately in the calculator.",
          "https://www.huaweicloud.com/intl/en-us/pricing/calculator.html#/ecs"),
    Offer("Huawei Cloud", "ECS x2.16u.64g (General Computing, X2)", 16, 64, "Not included", "Singapore", False,
          "$359.93 for 1 month ($0.6848/hr pay-per-use)", "USD", 359.93, SUBSCRIPTION, "Yes", "Confirmed", "2026-11-17",
          "Same type and price as the Jakarta row. CPU type not stated. AP-Singapore also has s3.4xlarge.4 at $336.38. "
          "Disk and bandwidth are priced separately in the calculator.",
          "https://www.huaweicloud.com/intl/en-us/pricing/calculator.html#/ecs"),
    Offer("Google Cloud", "Compute Engine e2-standard-16", 16, 64, "Not included", "Jakarta", True,
          f"$0.720848768/hr x {HOURS} h", "USD", round(0.720848768 * HOURS, 2), ON_DEMAND, "Yes", "Confirmed", "2026-11-17",
          f"Hourly price only: the monthly figure is {HOURS} hours of Linux on-demand use, with no commitment. "
          "Cheapest general-purpose 16 vCPU / 64 GB type in Jakarta. CPU type not stated. Disk is extra. n4-standard-16 is $0.9757/hr.",
          "https://cloud.google.com/products/compute/pricing/general-purpose"),
    Offer("Google Cloud", "Compute Engine e2-standard-16", 16, 64, "Not included", "Singapore", False,
          f"$0.66132912/hr x {HOURS} h", "USD", round(0.66132912 * HOURS, 2), ON_DEMAND, "Yes", "Confirmed", "2026-11-17",
          f"Hourly price only: the monthly figure is {HOURS} hours of Linux on-demand use, with no commitment. "
          "Same type as the Jakarta row; Singapore is 8% cheaper. CPU type not stated. Disk is extra.",
          "https://cloud.google.com/products/compute/pricing/general-purpose"),
    Offer("AWS EC2", "m7i-flex.4xlarge (general purpose, Intel)", 16, 64, "Not included (EBS)", "Jakarta", True,
          f"$0.9576/hr x {HOURS} h", "USD", round(0.9576 * HOURS, 2), ON_DEMAND, "Yes", "Confirmed", "2026-11-17",
          f"Hourly price only: the monthly figure is {HOURS} hours of Linux on-demand use, with no commitment. "
          "Cheapest x86 16 vCPU / 64 GiB type in Jakarta. CPU type not stated. The non-flex m6i.4xlarge is $0.96/hr ($700.80). Disk (EBS) is extra. The ARM type m6g.4xlarge is $0.768/hr "
          "($560.64), if the apps run on ARM. Lightsail (above) is AWS's fixed-price option.",
          "https://aws.amazon.com/ec2/pricing/on-demand/"),
    Offer("AWS EC2", "m7i-flex.4xlarge (general purpose, Intel)", 16, 64, "Not included (EBS)", "Singapore", False,
          f"$0.9576/hr x {HOURS} h", "USD", round(0.9576 * HOURS, 2), ON_DEMAND, "Yes", "Confirmed", "2026-11-17",
          f"Hourly price only: the monthly figure is {HOURS} hours of Linux on-demand use, with no commitment. "
          "Same type and price as the Jakarta row. CPU type not stated. Disk (EBS) is extra. Singapore also has m6a.4xlarge (AMD) at $0.864/hr.",
          "https://aws.amazon.com/ec2/pricing/on-demand/"),
    Offer("Tencent Cloud", "Cloud Virtual Machine", None, None, "-", "Jakarta", True,
          "Not read", "USD", None, "-", "Not confirmed (plan list could not be read)", CONSOLE_ONLY, "2026-11-17",
          "Tencent Cloud has a Jakarta region. Sizes and prices need a manual look in its price calculator.",
          "https://www.tencentcloud.com/pricing/cvm/overview"),
    Offer("Tencent Cloud", "Cloud Virtual Machine", None, None, "-", "Singapore", False,
          "Not read", "USD", None, "-", "Not confirmed (plan list could not be read)", CONSOLE_ONLY, "2026-11-17",
          "Sizes and prices need a manual look in its price calculator.",
          "https://www.tencentcloud.com/pricing/cvm/overview"),
]


def usd(o: Offer) -> float | None:
    return None if o.amount is None else round(o.amount / PER_USD[o.currency], 2)


def sorted_offers() -> list[Offer]:
    """Plans that fit first, cheapest first; unconfirmed prices last in their group."""
    return sorted(OFFERS, key=lambda o: (o.fits != "Yes", o.amount is None, usd(o) or 0, o.provider, o.location))


def evidence_key(o: Offer) -> str:
    return f"{o.provider} | {o.plan} | {o.location}"


def indonesia_text(o: Offer) -> str:
    return {True: "Yes", False: "No", None: "Not confirmed"}[o.in_indonesia]


def build_providers(wb) -> None:
    if "VPS Providers" in wb.sheetnames:
        del wb["VPS Providers"]
    ws = wb.create_sheet("VPS Providers")
    for c, h in enumerate(PROVIDER_HEADER, start=1):
        ws.cell(1, c, h).font = Font(bold=True)
    offers = sorted_offers()
    for r, o in enumerate(offers, start=2):
        row = [o.provider, o.plan, o.vcpu, o.ram_gb, o.disk, o.location, indonesia_text(o),
               o.price_text, usd(o), o.billing, o.fits, o.status, o.checked, o.notes, o.link]
        for c, v in enumerate(row, start=1):
            ws.cell(r, c, v)
        ws.cell(r, 9).number_format = "$#,##0.00"
        link = ws.cell(r, 15)
        link.hyperlink = o.link
        link.style = "Hyperlink"
    last = len(offers) + 1
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = f"A1:O{last}"
    ws.cell(last + 2, 1, f"Prices exclude tax where the provider states it; see Notes. Each price was checked on the date in its row. Rates per 1 USD on {RATES_DATE} "
                         f"(ECB via frankfurter.app): EUR {PER_USD['EUR']}, IDR {PER_USD['IDR']:,}, SGD {PER_USD['SGD']}. "
                         "Hourly-billed servers cost far less than the monthly cap if deleted after Day 5.")
    for col, width in zip("ABCDEFGHIJKLMNO", [15, 46, 6, 9, 24, 16, 13, 40, 16, 32, 22, 30, 11, 90, 46]):
        ws.column_dimensions[col].width = width


def build() -> None:
    wb = openpyxl.load_workbook(XLSX)
    ws = wb.active
    ws.delete_rows(2, ws.max_row)
    ws.cell(1, 8, "Notes")

    for r, (item, plan, period, qty, price, note) in enumerate(ROWS, start=2):
        for c, v in enumerate([item, plan, period, qty, price, TAX, f"=(1+F{r})*E{r}*D{r}", note], start=1):
            ws.cell(r, c, v)
        ws.cell(r, 5).number_format = "$#,##0.00"
        ws.cell(r, 6).number_format = "0%"
        ws.cell(r, 7).number_format = "$#,##0.00"

    last = 1 + len(ROWS)
    gt = last + 1
    ws.cell(gt, 1, "Grand Total").font = Font(bold=True)
    g = ws.cell(gt, 7, f"=SUM(G2:G{last})")
    g.font = Font(bold=True)
    g.number_format = "$#,##0.00"
    ws.cell(gt + 2, 1, NOTE)
    ws.cell(gt + 3, 1, ASSUMPTION)

    for col, width in zip("ABCDEFGH", [44, 62, 10, 10, 10, 9, 14, 90]):
        ws.column_dimensions[col].width = width
    build_providers(wb)
    wb.save(XLSX)


if __name__ == "__main__":
    try:
        build()
    except PermissionError:  # Excel holds the file: opening or saving it fails
        raise SystemExit("Close budgetting.xlsx in Excel, then rerun") from None
