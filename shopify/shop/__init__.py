import os

from shopify.shop import interface


shops = {
    i.shop_url: i
    for i in [
        interface.Shop(
            "HawaiianHealing",
            "hawaiianhealing",
            os.getenv("HAWAIIANHEALING_TOKEN", ""),
        ),
        # interface.Shop(
        #     "benzarid",
        #     "benzarid",
        #     os.getenv("benzarid_TOKEN", ""),
        # ),
        interface.Shop(
            "BedBugStore",
            "bedbugstore",
            os.getenv("BEDBUGSTORE_TOKEN", ""),
        ),
        interface.Shop(
            "Naturasil",
            "naturasil",
            os.getenv("NATURASIL_TOKEN", ""),
        ),
    ]
}
