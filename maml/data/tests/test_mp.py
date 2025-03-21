import unittest

from pymatgen.util.testing import PymatgenTest
from pymatgen.core import SETTINGS

from maml.data._mp import MaterialsProject


@unittest.skipIf(not SETTINGS.get("PMG_MAPI_KEY"), "PMG_MAPI_KEY environment variable not set")
class MaterialsProjectTest(PymatgenTest):
    def test_get(self):
        mp = MaterialsProject(SETTINGS.get("PMG_MAPI_KEY"))
        features = ["pretty_formula", "band_gap", "formation_energy_per_atom", "e_above_hull", "elasticity.K_VRH"]
        df = mp.get(criteria={"nelements": 1}, properties=features)
        assert df.shape[0] > 700
        assert df.shape[1] == len(features)
        assert set(df.columns) == set(features)


if __name__ == "__main__":
    unittest.main()
