# VPS price evidence

Where each confirmed price in the `VPS Providers` sheet of `budgetting.xlsx` was read. One line per row of the sheet. `tools/check_budget.py` fails if a confirmed row has no line here.

"How read" says what was fetched: the page's HTML with `curl`, or the provider's public API. Quotes are copied from the response; `...` marks text left out.

| Offer | URL | How read | Quote |
|---|---|---|---|
| Vultr \| Cloud Compute Regular vc2-16c-64gb \| Singapore | https://api.vultr.com/v2/plans | Public API, 2026-11-17 | `"id": "vc2-16c-64gb", "vcpu_count": 16, "ram": 65536, "disk": 1280, "monthly_cost": 320, "hourly_cost": 0.438, "location_cost": {}`; `locations` includes `sgp`. `/v2/regions` lists no region in Indonesia. |
| Vultr \| Optimized Cloud General Purpose voc-g-16c-64gb-320s-amd \| Singapore | https://api.vultr.com/v2/plans | Public API, 2026-11-17 | `"id": "voc-g-16c-64gb-320s-amd", "vcpu_count": 16, "ram": 65536, "disk": 320, "monthly_cost": 480, "hourly_cost": 0.658, "location_cost": {}`; `locations` includes `sgp`. |
| Hetzner \| CCX43 (dedicated vCPU) \| Singapore | https://www.hetzner.com/cloud/general-purpose | Page HTML, 2026-11-17 | CCX43 row, price element `location="SIN1"`: "€ 341.49 per month, excl. VAT". Row: "CCX43 16 AMD 64 GB 360 GB NVMe". Page: "Price incl. IPv4". |
| Hetzner \| CCX43 (dedicated vCPU) \| Helsinki | https://www.hetzner.com/cloud/general-purpose | Page HTML, 2026-11-17 | CCX43 row, price element `location="HEL1"`: "€ 234.99 per month, excl. VAT". Other locations in the same row: NBG1 € 276.49, HIL1 and ASH1 € 279.99. |
| Hetzner \| CPX62 (shared vCPU) \| Singapore | https://www.hetzner.com/cloud/regular-performance | Page HTML, 2026-11-17 | CPX62 row, price element `location="SIN1"`: "€ 172.49 per month, excl. VAT". Row: "CPX62 16 AMD 32 GB 640 GB NVMe". HEL1 € 110.99, NBG1 € 130.49. |
| Akamai Linode \| Shared CPU Linode 64GB (g6-standard-16) \| Jakarta | https://api.linode.com/v4/linode/types | Public API, 2026-11-17 | `g6-standard-16`, label "Linode 64GB", `region_prices`: `{"id": "id-cgk", "hourly": 0.691, "monthly": 460.8}`. `/v4/regions`: `id-cgk` = "Jakarta, ID". |
| Akamai Linode \| Shared CPU Linode 64GB (g6-standard-16) \| Singapore | https://api.linode.com/v4/linode/types | Public API, 2026-11-17 | `g6-standard-16`, `"price": {"hourly": 0.576, "monthly": 384.0}`; `region_prices` holds only `id-cgk` and `br-gru`, so Singapore (`ap-south`, `sg-sin-2`) is at the standard price. |
| AWS Lightsail \| Linux bundle 64 GB / 16 vCPU, public IPv4 \| Jakarta | https://aws.amazon.com/lightsail/pricing/ | Page HTML, 2026-11-17 | Under "Bundles with public IPv4 address", Linux/Unix, General Purpose: "$384 USD/mo 64 GB Memory 16 vCPUs 1280 GB SSD Disk 8 TB Transfer*". The page gives one bundle list for all Regions, and: "Plans in Asia Pacific (Mumbai), Asia Pacific (Sydney), Asia Pacific (Jakarta) ... Regions include half the data transfer allowances mentioned in the bundles above." |
| AWS Lightsail \| Linux bundle 64 GB / 16 vCPU, public IPv4 \| Singapore | https://aws.amazon.com/lightsail/pricing/ | Page HTML, 2026-11-17 | Same bundle line: "$384 USD/mo 64 GB Memory 16 vCPUs 1280 GB SSD Disk 8 TB Transfer*". Singapore is not in the list of Regions with half the transfer allowance. |
| UpCloud \| Premium 64 GB / 16 cores \| Singapore | https://upcloud.com/pricing/ | Page HTML, 2026-11-17 | Under "Premium", table "Memory / CPU cores / MaxIOPS / Price", marked "Global price": "64 GB 16 300 GB €384/mo". "Premium plans are billed by the starting hour, maximum of 28 days per month. Prices exclude any applicable local taxes." Data centre list (https://upcloud.com/data-centres/): "Singapore, Singapore SG-SIN1". |
| DigitalOcean \| General Purpose Droplet g-16vcpu-64gb (dedicated vCPU) \| Singapore | https://www.digitalocean.com/pricing/droplets | Page HTML, 2026-11-17 | General Purpose table row linking to `size=g-16vcpu-64gb`: "64 GiB, 16 vCPUs, 7,000 GiB, 200 GiB, $0.75000, $504.00". The page has no per-region price. |
| Contabo \| Cloud VPS 16 \| Singapore | https://contabo.com/en/vps/cloud-vps-core-16 | Page HTML and the order form's data in the same page, 2026-11-17 | Term: "1 Month €37.00 / month No Setup Fee ... 12 Months ... €31.45 / month ... 24 Months ... €29.60 / month". Location option: `title: "Asia (Singapore)", slug: "location-singapore-cloud-vps-16", price: {EUR: 20.75, GBP: 20.75, USD: 25.75}, setupPrice: {EUR: 0, ...}, outOfStock: true`. 37.00 + 20.75 = 57.75. |
| Contabo \| Cloud VPS 16 \| European Union | https://contabo.com/en/vps/cloud-vps-core-16 | Page HTML, 2026-11-17 | "1 Month €37.00 / month No Setup Fee". Order summary with the default region: "Contract Period: 1 Month ... European Union ... Monthly €37.00 One-Time €0.00". |
| Biznet Gio \| NEO Lite LL 16.16 (largest NEO Lite) \| Indonesia | https://www.biznetgio.com/product/neo-lite | Page HTML, 2026-11-17 | "NEO Lite LL 16.16 16 Core vCPU 16 GB RAM 60GB SSD Storage ... Rp998.000 Rp499.000 / bulan" (first figure struck through). "Diskon Hingga 50% Khusus Pengguna Baru". "Data Center di Indonesia". |

## Not confirmed

| Offer | URL | What the site showed | Why it is not confirmed |
|---|---|---|---|
| OVHcloud \| VPS-4 (largest VPS) \| Singapore | https://www.ovhcloud.com/en-sg/vps/ | "VPS-4 From S$30 ex. GST/month ... 8 vCores 24 GB RAM 200 GB SSD NVMe" | A "from" price on the Singapore-currency site. The page does not say which data centre or which commitment it applies to. |
