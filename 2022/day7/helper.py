def set_nested_value(dic, keys, value, create_missing=True):
  d = dic
  for key in keys[:-1]:
      if key in d:
          d = d[key]
      elif create_missing:
          d = d.setdefault(key, {})
      else:
          return dic
  if keys[-1] in d or create_missing:
      d[keys[-1]] = value
  return dic

def get_nested_value(dic, keys):
  d = dic
  for key in keys:
    d = d[key]
  return d

def calc_dir_size(fs: dict, ignore=""):
  size = 0
  for k in fs.keys():
    if ignore == k:
      continue
    size += calc_dir_size(fs[k]) if type(fs[k]) == dict else fs[k]
  return size