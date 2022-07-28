# Download of digiS metadata

Download from [Deutsche Digitale Bibliothek](https://www.deutsche-digitale-bibliothek.de/) was performed on 28/7/2022 with code modelled after `download.py`.

The overwhelming majority of the metadata is CC0.

The following command provides an overview of the `rightsType` values:

```bash
for i in lido/*xml
  do xmlstarlet sel -N lido=http://www.lido-schema.org -t -v '//lido:recordWrap//lido:rightsType/lido:conceptID' -n $i
done | sort | uniq -c | sort -n
```

| # | licence | 
| --- | --- | 
| 577 | https://creativecommons.org/licenses/by/4.0/ |
| 637 | https://creativecommons.org/publicdomain/zero/1.0/deed.de |
| 8093 | https://creativecommons.org/publicdomain/zero/1.0/ |
| 12143 | http://creativecommons.org/publicdomain/zero/1.0/deed.de |
| 29019 | http://creativecommons.org/publicdomain/zero/1.0/ |

The 577 CC-BY-licensed data belong to the [Landesgeschichtliche Vereinigung für die Mark Brandenburg e.V.](https://www.deutsche-digitale-bibliothek.de/organization/HZOJ7KGT4ICOQVASW67GS23VPYVUPR7G)

```bash
for i in digiS_data/lido/*.xml
  do xmlstarlet sel -N lido=http://www.lido-schema.org -t -v '//lido:recordWrap//lido:rightsType/lido:conceptID[.="https://creativecommons.org/licenses/by/4.0/"]/../../lido:rightsHolder/lido:legalBodyName/lido:appellationValue' -n $i
done | grep -v '^$' | sort | uniq -c
```

A list of these files can be produced as follows

```bash
for i in digiS_data/lido/*.xml
  do xmlstarlet sel -N lido=http://www.lido-schema.org -t -i '//lido:recordWrap//lido:rightsType/lido:conceptID[.="https://creativecommons.org/licenses/by/4.0/"]/../../lido:rightsHolder/lido:legalBodyName/lido:appellationValue' -f -n $i
done
```
