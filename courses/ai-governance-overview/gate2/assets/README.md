# World map source

`world.geojson` contains Natural Earth's public-domain 1:110m country outlines.
Retrieved 12 September 2026 from:
https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_110m_admin_0_countries.geojson

Natural Earth terms: https://www.naturalearthdata.com/about/terms-of-use/

`build.py` projects the geometry to an inline SVG and highlights the selected EU members and UK, with a location marker for Singapore. The map is an orientation aid, not a determination of territorial legal scope. Some small territories are absent at this map scale. No network request is needed during presentation.
