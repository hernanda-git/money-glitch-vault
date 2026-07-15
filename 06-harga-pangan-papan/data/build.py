import json, sys, datetime
def round2(x):
    try: return round(float(x),2)
    except (TypeError,ValueError): return None
def build(api_path, data_date, prev_date):
    api=json.load(open(api_path,encoding='utf-8'))
    rows_out=[]; commodity_names=[]
    for item in api['data']:
        name=item.get('variant_nama'); unit=item.get('satuan_display')
        if name not in commodity_names: commodity_names.append(name)
        harga=item.get('harga'); hprev=item.get('harga_pembanding')
        rows_out.append({"date":data_date,"commodity_name":name,"unit":unit,"region":"Nasional",
            "previous_price":(hprev if hprev is not None else None),
            "current_price":(harga if harga is not None else None),
            "change_percent":round2(item.get('persen_perubahan')) if (harga is not None or hprev is not None) else None})
        for reg in (item.get('region') or []):
            rh=reg.get('harga'); rhp=reg.get('harga_pembanding')
            rows_out.append({"date":data_date,"commodity_name":name,"unit":reg.get('satuan_display',unit),
                "region":reg.get('region'),
                "previous_price":(rhp if rhp is not None else None),
                "current_price":(rh if rh is not None else None),
                "change_percent":round2(reg.get('persen_perubahan')) if (rh is not None or rhp is not None) else None})
    return {"source":"api-sp2kp.kemendag.go.id (REST: report/api/average-price/generate-perbandingan-harga)",
        "fetched_at_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "data_date":data_date,"previous_date":prev_date,
        "commodity_count":len(commodity_names),"row_count":len(rows_out),
        "commodity_names":commodity_names,"rows":rows_out}
if __name__=='__main__':
    api_path,data_date,prev_date,out_path=sys.argv[1:5]
    out=build(api_path,data_date,prev_date)
    json.dump(out,open(out_path,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
    nreg=len([r for r in out['rows'] if r['region']!='Nasional'])
    print(f"{out_path}: {out['commodity_count']} commodities, {out['row_count']} rows ({nreg} regions)")
