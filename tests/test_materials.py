"""检查合成资料的关键业务关系，避免错误输入被误作有效资料。"""
import unittest
import numpy as np
from inspect_data import load_materials

class MaterialIntegrity(unittest.TestCase):
    def test_domain_relationships(self):
        v,a=load_materials()
        pts=v['objects']['points']
        self.assertEqual(pts[0]['xyz'],pts[1]['xyz'])
        self.assertNotEqual(pts[0]['label'],pts[1]['label'])
        self.assertEqual(len(v['objects']['offsets']),27)
        self.assertEqual(len({tuple(x) for x in v['objects']['offsets']}),27)
        for layer in v['objects']['layers']:
            self.assertEqual(a[layer['weight']].shape,(27,layer['output_channels'],layer['input_channels']))
        self.assertEqual({p['arrival_phase'] for p in pts},{1,2})

if __name__ == '__main__':
    unittest.main()
