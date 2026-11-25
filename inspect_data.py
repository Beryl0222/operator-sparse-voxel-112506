"""检查合成资料的数组布局、身份和引用，供产品资料维护使用。"""
import json
from pathlib import Path
import numpy as np

def load_materials(path=None):
    path = Path(path) if path else Path(__file__).parent / 'data/small.json'
    value = json.loads(path.read_text(encoding='utf-8'))
    arrays = {name: np.asarray(content) for name, content in value['tensors'].items()}
    for name, arr in arrays.items():
        if arr.dtype.kind not in 'biuf' or not np.isfinite(arr).all():
            raise ValueError('数值资料不是有限实数数组：' + name)
    return value, arrays

def main():
    value, arrays = load_materials()
    print(json.dumps({'项目': value['product'], '资料性质': value['nature'], '数组': {k: {'shape': list(v.shape), 'dtype': str(v.dtype)} for k,v in arrays.items()}, '数据对象': list(value['objects'])}, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
