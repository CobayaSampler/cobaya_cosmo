cmb = {
    # Planck #############################################################################
    "planck_PR4_lollipop.lowlE": {
        "class": "planck_2020_lollipop.lowlE",
        "desc": "sth...",
        "biburl": "http...",
        "package_install": {
            "pip": "planck_2020_lollipop",
            "min_version": "4.1.1",
        },
    },
    "planck_PR4_lollipop.lowlB": {
        "class": "planck_2020_lollipop.lowlB",
        "desc": "sth...",
        "biburl": "http...",
        "package_install": {
            "pip": "planck_2020_lollipop",
            "min_version": "4.1.1",
        },
    },
    "planck_PR4_lollipop.lowlEB": {
        "class": "planck_2020_lollipop.lowlEB",
        "desc": "sth...",
        "biburl": "http...",
        "package_install": {
            "pip": "planck_2020_lollipop",
            "min_version": "4.1.1",
        },
    },
    "planck_PR4_hillipop.TT": {
        "class": "planck_2020_hillipop.TT",
        "desc": "sth...",
        "biburl": "http...",
        "package_install": {
            "pip": "planck_2020_hillipop",
            "min_version": "4.2.2",
        },
    },
    "planck_PR4_hillipop.TE": {
        "class": "planck_2020_hillipop.TE",
        "desc": "sth...",
        "biburl": "http...",
        "package_install": {
            "pip": "planck_2020_hillipop",
            "min_version": "4.2.2",
        },
    },
    "planck_PR4_hillipop.EE": {
        "class": "planck_2020_hillipop.EE",
        "desc": "sth...",
        "biburl": "http...",
        "package_install": {
            "pip": "planck_2020_hillipop",
            "min_version": "4.2.2",
        },
    },
    "planck_PR4_hillipop.TTTEEE": {
        "class": "planck_2020_hillipop.TTTEEE",
        "desc": "sth...",
        "biburl": "http...",
        "package_install": {
            "pip": "planck_2020_hillipop",
            "min_version": "4.2.2",
        },
    },
    "planck_PR4_lensing": {
        "class": "planckpr4lensing",
        "desc": "Planck PR4 (NPIPE) lensing likelihoods, by J. Carron, M. Mirmelstein and A. Lewis, together with the Planck PR4 ISW-lensing likelihoods by J. Carron, G. Fabbian and A. Lewis",
        "biburl": ["https://arxiv.org/abs/2007.04997", "https://arxiv.org/abs/2005.05290"],
        "package_install": {
            "github_repository": "carronj/planck_PR4_lensing",
            "min_version": "1.0.2",
        },
    },
    # ACT ################################################################################
    "act_dr4_lite": {
        "class": "pyactlike.ACTPol_lite_DR4",
        "desc": "Atacama Cosmology Telescope DR4 CMB power spectrum likelihood, already marginalized over SZ and foreground emission; based on the WMAP and ACT team's likelihood software.",
        "biburl": ["https://arxiv.org/abs/2007.07288", "https://arxiv.org/abs/2007.07289"],
        "package_install": {
            "github_repository": "ACTCollaboration/pyactlike",  # BRANCH cobaya_updates???
        },
    },
    "act_dr4_lite_for_planck_combination": {
        "class": "pyactlike.ACTPol_lite_DR4_for_combining_with_planck",
        "desc": "Atacama Cosmology Telescope DR4 CMB power spectrum likelihood, already marginalized over SZ and foreground emission, with a multipole cut to avoid correlations with Plank; based on the WMAP and ACT team's likelihood software.",
        "biburl": ["https://arxiv.org/abs/2007.07288", "https://arxiv.org/abs/2007.07289"],
        "package_install": {
            "github_repository": "ACTCollaboration/pyactlike", # BRANCH cobaya_updates???
        },
    },
    "act_dr6_lenslike": {
        "class": "act_dr6_lenslike.ACTDR6LensLike",
        "desc": "...",
        "biburl": ["https://arxiv.org/abs/2304.05203", "https://arxiv.org/abs/2304.05202"],
        "package_install": {
            "pip": "act_dr6_lenslike",
            "min_version": "1.2.0",
        },
    },
    # SPT ################################################################################
    "sptpol_2017.TEEE": {
        "class": "sptpol_2017.TEEE",
        "desc": "...",
        "biburl": "https://arxiv.org/abs/1707.09353",
        "package_install": {
            "github_repository": "xgarrido/spt_likelihoods",
        },
    },
    "spt3g_2020.TEEE": {
        "class": "spt3g_2020.TEEE",
        "desc": "...",
        "biburl": "https://arxiv.org/abs/2101.01684",
        "package_install": {
            "github_repository": "xgarrido/spt_likelihoods",
        },
    },
    "spt_hiell_2020.TT": {
        "class": "spt_hiell_2020.TT",
        "desc": "...",
        "biburl": "https://arxiv.org/abs/2002.06197",
        "package_install": {
            "github_repository": "xgarrido/spt_likelihoods",
        },
    },
    "spt3g_2022.TT": {
        "class": "spt3g_2022.TT",
        "desc": "...",
        "biburl": "https://arxiv.org/abs/2212.05642",
        "package_install": {
            "github_repository": "xgarrido/spt_likelihoods",
        },
    },
    "spt3g_2022.TE": {
        "class": "spt3g_2022.TE",
        "desc": "",
        "biburl": "https://arxiv.org/abs/2212.05642",
        "package_install": {
            "github_repository": "xgarrido/spt_likelihoods",
        },
    },
    "spt3g_2022.EE": {
        "class": "spt3g_2022.EE",
        "desc": "...",
        "biburl": "https://arxiv.org/abs/2212.05642",
        "package_install": {
            "github_repository": "xgarrido/spt_likelihoods",
        },
    },
    "spt3g_2022.TTTEEE": {
        "class": "spt3g_2022.TTTEEE",
        "desc": "...",
        "biburl": "https://arxiv.org/abs/2212.05642",
        "package_install": {
            "github_repository": "xgarrido/spt_likelihoods",
        },
    },
}
