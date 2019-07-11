Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> path="C:\Program Files\Python36\cardata.csv.txt"
>>> df=pd.read_csv(path)
>>> df.head(5)
   3    ?  alfa-romero  gas  std   two  ...  9.00  111  5000  21  27  13495
0  3    ?  alfa-romero  gas  std   two  ...   9.0  111  5000  21  27  16500
1  1    ?  alfa-romero  gas  std   two  ...   9.0  154  5000  19  26  16500
2  2  164         audi  gas  std  four  ...  10.0  102  5500  24  30  13950
3  2  164         audi  gas  std  four  ...   8.0  115  5500  18  22  17450
4  2    ?         audi  gas  std   two  ...   8.5  110  5500  19  25  15250

[5 rows x 26 columns]
>>> #DATA CLEANING and DATA WRANGLING
>>> headers=["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors","bodystyle","drive-wheels","engine-location","wheelbase","length","width","height","curved-weight" ,"engine-type","num-of-cylinder" ,"engine-size","system", "boar","stroke", "compression-ratio","horse-power","peak-rpm", "city","highway-mpg","price"]
>>> df.columns=headers
>>> df.head(4)
   symboling normalized-losses         make  ... city highway-mpg  price
0          3                 ?  alfa-romero  ...   21          27  16500
1          1                 ?  alfa-romero  ...   19          26  16500
2          2               164         audi  ...   24          30  13950
3          2               164         audi  ...   18          22  17450

[4 rows x 26 columns]
>>> df.tail(4)
     symboling normalized-losses   make  ... city highway-mpg  price
200         -1                95  volvo  ...   19          25  19045
201         -1                95  volvo  ...   18          23  21485
202         -1                95  volvo  ...   26          27  22470
203         -1                95  volvo  ...   19          25  22625

[4 rows x 26 columns]
>>> df.dtypes
symboling              int64
normalized-losses     object
make                  object
fuel-type             object
aspiration            object
num-of-doors          object
bodystyle             object
drive-wheels          object
engine-location       object
wheelbase            float64
length               float64
width                float64
height               float64
curved-weight          int64
engine-type           object
num-of-cylinder       object
engine-size            int64
system                object
boar                  object
stroke                object
compression-ratio    float64
horse-power           object
peak-rpm              object
city                   int64
highway-mpg            int64
price                 object
dtype: object
>>> pd.set_option('display.max_columns',24)
>>> pd.set_option('display.max_columns',26)
>>> df.describe(include="all")
         symboling normalized-losses    make fuel-type aspiration  \
count   204.000000               204     204       204        204   
unique         NaN                52      22         2          2   
top            NaN                 ?  toyota       gas        std   
freq           NaN                40      32       184        167   
mean      0.823529               NaN     NaN       NaN        NaN   
std       1.239035               NaN     NaN       NaN        NaN   
min      -2.000000               NaN     NaN       NaN        NaN   
25%       0.000000               NaN     NaN       NaN        NaN   
50%       1.000000               NaN     NaN       NaN        NaN   
75%       2.000000               NaN     NaN       NaN        NaN   
max       3.000000               NaN     NaN       NaN        NaN   

       num-of-doors bodystyle drive-wheels engine-location   wheelbase  \
count           204       204          204             204  204.000000   
unique            3         5            3               2         NaN   
top            four     sedan          fwd           front         NaN   
freq            114        96          120             201         NaN   
mean            NaN       NaN          NaN             NaN   98.806373   
std             NaN       NaN          NaN             NaN    5.994144   
min             NaN       NaN          NaN             NaN   86.600000   
25%             NaN       NaN          NaN             NaN   94.500000   
50%             NaN       NaN          NaN             NaN   97.000000   
75%             NaN       NaN          NaN             NaN  102.400000   
max             NaN       NaN          NaN             NaN  120.900000   

            length       width      height  curved-weight engine-type  \
count   204.000000  204.000000  204.000000     204.000000         204   
unique         NaN         NaN         NaN            NaN           7   
top            NaN         NaN         NaN            NaN         ohc   
freq           NaN         NaN         NaN            NaN         148   
mean    174.075000   65.916667   53.749020    2555.602941         NaN   
std      12.362123    2.146716    2.424901     521.960820         NaN   
min     141.100000   60.300000   47.800000    1488.000000         NaN   
25%     166.300000   64.075000   52.000000    2145.000000         NaN   
50%     173.200000   65.500000   54.100000    2414.000000         NaN   
75%     183.200000   66.900000   55.500000    2939.250000         NaN   
max     208.100000   72.300000   59.800000    4066.000000         NaN   

       num-of-cylinder  engine-size system  boar stroke  compression-ratio  \
count              204   204.000000    204   204    204         204.000000   
unique               7          NaN      8    39     37                NaN   
top               four          NaN   mpfi  3.62   3.40                NaN   
freq               158          NaN     93    23     20                NaN   
mean               NaN   126.892157    NaN   NaN    NaN          10.148137   
std                NaN    41.744569    NaN   NaN    NaN           3.981000   
min                NaN    61.000000    NaN   NaN    NaN           7.000000   
25%                NaN    97.000000    NaN   NaN    NaN           8.575000   
50%                NaN   119.500000    NaN   NaN    NaN           9.000000   
75%                NaN   142.000000    NaN   NaN    NaN           9.400000   
max                NaN   326.000000    NaN   NaN    NaN          23.000000   

       horse-power peak-rpm        city  highway-mpg price  
count          204      204  204.000000   204.000000   204  
unique          60       24         NaN          NaN   186  
top             68     5500         NaN          NaN     ?  
freq            19       37         NaN          NaN     4  
mean           NaN      NaN   25.240196    30.769608   NaN  
std            NaN      NaN    6.551513     6.898337   NaN  
min            NaN      NaN   13.000000    16.000000   NaN  
25%            NaN      NaN   19.000000    25.000000   NaN  
50%            NaN      NaN   24.000000    30.000000   NaN  
75%            NaN      NaN   30.000000    34.500000   NaN  
max            NaN      NaN   49.000000    54.000000   NaN  
>>> df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 204 entries, 0 to 203
Data columns (total 26 columns):
symboling            204 non-null int64
normalized-losses    204 non-null object
make                 204 non-null object
fuel-type            204 non-null object
aspiration           204 non-null object
num-of-doors         204 non-null object
bodystyle            204 non-null object
drive-wheels         204 non-null object
engine-location      204 non-null object
wheelbase            204 non-null float64
length               204 non-null float64
width                204 non-null float64
height               204 non-null float64
curved-weight        204 non-null int64
engine-type          204 non-null object
num-of-cylinder      204 non-null object
engine-size          204 non-null int64
system               204 non-null object
boar                 204 non-null object
stroke               204 non-null object
compression-ratio    204 non-null float64
horse-power          204 non-null object
peak-rpm             204 non-null object
city                 204 non-null int64
highway-mpg          204 non-null int64
price                204 non-null object
dtypes: float64(5), int64(5), object(16)
memory usage: 41.5+ KB
>>> df.replace(to_replace="?",value="0",inplace=True) #Cleaning unnecesary data
>>> df.head(23)
    symboling normalized-losses         make fuel-type aspiration  \
0           3                 0  alfa-romero       gas        std   
1           1                 0  alfa-romero       gas        std   
2           2               164         audi       gas        std   
3           2               164         audi       gas        std   
4           2                 0         audi       gas        std   
5           1               158         audi       gas        std   
6           1                 0         audi       gas        std   
7           1               158         audi       gas      turbo   
8           0                 0         audi       gas      turbo   
9           2               192          bmw       gas        std   
10          0               192          bmw       gas        std   
11          0               188          bmw       gas        std   
12          0               188          bmw       gas        std   
13          1                 0          bmw       gas        std   
14          0                 0          bmw       gas        std   
15          0                 0          bmw       gas        std   
16          0                 0          bmw       gas        std   
17          2               121    chevrolet       gas        std   
18          1                98    chevrolet       gas        std   
19          0                81    chevrolet       gas        std   
20          1               118        dodge       gas        std   
21          1               118        dodge       gas        std   
22          1               118        dodge       gas      turbo   

   num-of-doors    bodystyle drive-wheels engine-location  wheelbase  length  \
0           two  convertible          rwd           front       88.6   168.8   
1           two    hatchback          rwd           front       94.5   171.2   
2          four        sedan          fwd           front       99.8   176.6   
3          four        sedan          4wd           front       99.4   176.6   
4           two        sedan          fwd           front       99.8   177.3   
5          four        sedan          fwd           front      105.8   192.7   
6          four        wagon          fwd           front      105.8   192.7   
7          four        sedan          fwd           front      105.8   192.7   
8           two    hatchback          4wd           front       99.5   178.2   
9           two        sedan          rwd           front      101.2   176.8   
10         four        sedan          rwd           front      101.2   176.8   
11          two        sedan          rwd           front      101.2   176.8   
12         four        sedan          rwd           front      101.2   176.8   
13         four        sedan          rwd           front      103.5   189.0   
14         four        sedan          rwd           front      103.5   189.0   
15          two        sedan          rwd           front      103.5   193.8   
16         four        sedan          rwd           front      110.0   197.0   
17          two    hatchback          fwd           front       88.4   141.1   
18          two    hatchback          fwd           front       94.5   155.9   
19         four        sedan          fwd           front       94.5   158.8   
20          two    hatchback          fwd           front       93.7   157.3   
21          two    hatchback          fwd           front       93.7   157.3   
22          two    hatchback          fwd           front       93.7   157.3   

    width  height  curved-weight engine-type num-of-cylinder  engine-size  \
0    64.1    48.8           2548        dohc            four          130   
1    65.5    52.4           2823        ohcv             six          152   
2    66.2    54.3           2337         ohc            four          109   
3    66.4    54.3           2824         ohc            five          136   
4    66.3    53.1           2507         ohc            five          136   
5    71.4    55.7           2844         ohc            five          136   
6    71.4    55.7           2954         ohc            five          136   
7    71.4    55.9           3086         ohc            five          131   
8    67.9    52.0           3053         ohc            five          131   
9    64.8    54.3           2395         ohc            four          108   
10   64.8    54.3           2395         ohc            four          108   
11   64.8    54.3           2710         ohc             six          164   
12   64.8    54.3           2765         ohc             six          164   
13   66.9    55.7           3055         ohc             six          164   
14   66.9    55.7           3230         ohc             six          209   
15   67.9    53.7           3380         ohc             six          209   
16   70.9    56.3           3505         ohc             six          209   
17   60.3    53.2           1488           l           three           61   
18   63.6    52.0           1874         ohc            four           90   
19   63.6    52.0           1909         ohc            four           90   
20   63.8    50.8           1876         ohc            four           90   
21   63.8    50.8           1876         ohc            four           90   
22   63.8    50.8           2128         ohc            four           98   

   system  boar stroke  compression-ratio horse-power peak-rpm  city  \
0    mpfi  3.47   2.68               9.00         111     5000    21   
1    mpfi  2.68   3.47               9.00         154     5000    19   
2    mpfi  3.19   3.40              10.00         102     5500    24   
3    mpfi  3.19   3.40               8.00         115     5500    18   
4    mpfi  3.19   3.40               8.50         110     5500    19   
5    mpfi  3.19   3.40               8.50         110     5500    19   
6    mpfi  3.19   3.40               8.50         110     5500    19   
7    mpfi  3.13   3.40               8.30         140     5500    17   
8    mpfi  3.13   3.40               7.00         160     5500    16   
9    mpfi  3.50   2.80               8.80         101     5800    23   
10   mpfi  3.50   2.80               8.80         101     5800    23   
11   mpfi  3.31   3.19               9.00         121     4250    21   
12   mpfi  3.31   3.19               9.00         121     4250    21   
13   mpfi  3.31   3.19               9.00         121     4250    20   
14   mpfi  3.62   3.39               8.00         182     5400    16   
15   mpfi  3.62   3.39               8.00         182     5400    16   
16   mpfi  3.62   3.39               8.00         182     5400    15   
17   2bbl  2.91   3.03               9.50          48     5100    47   
18   2bbl  3.03   3.11               9.60          70     5400    38   
19   2bbl  3.03   3.11               9.60          70     5400    38   
20   2bbl  2.97   3.23               9.41          68     5500    37   
21   2bbl  2.97   3.23               9.40          68     5500    31   
22   mpfi  3.03   3.39               7.60         102     5500    24   

    highway-mpg  price  
0            27  16500  
1            26  16500  
2            30  13950  
3            22  17450  
4            25  15250  
5            25  17710  
6            25  18920  
7            20  23875  
8            22      0  
9            29  16430  
10           29  16925  
11           28  20970  
12           28  21105  
13           25  24565  
14           22  30760  
15           22  41315  
16           20  36880  
17           53   5151  
18           43   6295  
19           43   6575  
20           41   5572  
21           38   6377  
22           30   7957  
>>> df=df.astype({"normalized-losses":float}) #Changing the Data type
>>> df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 204 entries, 0 to 203
Data columns (total 26 columns):
symboling            204 non-null int64
normalized-losses    204 non-null float64
make                 204 non-null object
fuel-type            204 non-null object
aspiration           204 non-null object
num-of-doors         204 non-null object
bodystyle            204 non-null object
drive-wheels         204 non-null object
engine-location      204 non-null object
wheelbase            204 non-null float64
length               204 non-null float64
width                204 non-null float64
height               204 non-null float64
curved-weight        204 non-null int64
engine-type          204 non-null object
num-of-cylinder      204 non-null object
engine-size          204 non-null int64
system               204 non-null object
boar                 204 non-null object
stroke               204 non-null object
compression-ratio    204 non-null float64
horse-power          204 non-null object
peak-rpm             204 non-null object
city                 204 non-null int64
highway-mpg          204 non-null int64
price                204 non-null object
dtypes: float64(6), int64(5), object(15)
memory usage: 41.5+ KB
>>> #SCALING
>>> mean_normal=df["normalized-losses"].mean()
>>> df["normalized-losses"].replace(to_replace="0",value=mean_normal,inplace=True)
>>> df.head(23)
    symboling  normalized-losses         make fuel-type aspiration  \
0           3                0.0  alfa-romero       gas        std   
1           1                0.0  alfa-romero       gas        std   
2           2              164.0         audi       gas        std   
3           2              164.0         audi       gas        std   
4           2                0.0         audi       gas        std   
5           1              158.0         audi       gas        std   
6           1                0.0         audi       gas        std   
7           1              158.0         audi       gas      turbo   
8           0                0.0         audi       gas      turbo   
9           2              192.0          bmw       gas        std   
10          0              192.0          bmw       gas        std   
11          0              188.0          bmw       gas        std   
12          0              188.0          bmw       gas        std   
13          1                0.0          bmw       gas        std   
14          0                0.0          bmw       gas        std   
15          0                0.0          bmw       gas        std   
16          0                0.0          bmw       gas        std   
17          2              121.0    chevrolet       gas        std   
18          1               98.0    chevrolet       gas        std   
19          0               81.0    chevrolet       gas        std   
20          1              118.0        dodge       gas        std   
21          1              118.0        dodge       gas        std   
22          1              118.0        dodge       gas      turbo   

   num-of-doors    bodystyle drive-wheels engine-location  wheelbase  length  \
0           two  convertible          rwd           front       88.6   168.8   
1           two    hatchback          rwd           front       94.5   171.2   
2          four        sedan          fwd           front       99.8   176.6   
3          four        sedan          4wd           front       99.4   176.6   
4           two        sedan          fwd           front       99.8   177.3   
5          four        sedan          fwd           front      105.8   192.7   
6          four        wagon          fwd           front      105.8   192.7   
7          four        sedan          fwd           front      105.8   192.7   
8           two    hatchback          4wd           front       99.5   178.2   
9           two        sedan          rwd           front      101.2   176.8   
10         four        sedan          rwd           front      101.2   176.8   
11          two        sedan          rwd           front      101.2   176.8   
12         four        sedan          rwd           front      101.2   176.8   
13         four        sedan          rwd           front      103.5   189.0   
14         four        sedan          rwd           front      103.5   189.0   
15          two        sedan          rwd           front      103.5   193.8   
16         four        sedan          rwd           front      110.0   197.0   
17          two    hatchback          fwd           front       88.4   141.1   
18          two    hatchback          fwd           front       94.5   155.9   
19         four        sedan          fwd           front       94.5   158.8   
20          two    hatchback          fwd           front       93.7   157.3   
21          two    hatchback          fwd           front       93.7   157.3   
22          two    hatchback          fwd           front       93.7   157.3   

    width  height  curved-weight engine-type num-of-cylinder  engine-size  \
0    64.1    48.8           2548        dohc            four          130   
1    65.5    52.4           2823        ohcv             six          152   
2    66.2    54.3           2337         ohc            four          109   
3    66.4    54.3           2824         ohc            five          136   
4    66.3    53.1           2507         ohc            five          136   
5    71.4    55.7           2844         ohc            five          136   
6    71.4    55.7           2954         ohc            five          136   
7    71.4    55.9           3086         ohc            five          131   
8    67.9    52.0           3053         ohc            five          131   
9    64.8    54.3           2395         ohc            four          108   
10   64.8    54.3           2395         ohc            four          108   
11   64.8    54.3           2710         ohc             six          164   
12   64.8    54.3           2765         ohc             six          164   
13   66.9    55.7           3055         ohc             six          164   
14   66.9    55.7           3230         ohc             six          209   
15   67.9    53.7           3380         ohc             six          209   
16   70.9    56.3           3505         ohc             six          209   
17   60.3    53.2           1488           l           three           61   
18   63.6    52.0           1874         ohc            four           90   
19   63.6    52.0           1909         ohc            four           90   
20   63.8    50.8           1876         ohc            four           90   
21   63.8    50.8           1876         ohc            four           90   
22   63.8    50.8           2128         ohc            four           98   

   system  boar stroke  compression-ratio horse-power peak-rpm  city  \
0    mpfi  3.47   2.68               9.00         111     5000    21   
1    mpfi  2.68   3.47               9.00         154     5000    19   
2    mpfi  3.19   3.40              10.00         102     5500    24   
3    mpfi  3.19   3.40               8.00         115     5500    18   
4    mpfi  3.19   3.40               8.50         110     5500    19   
5    mpfi  3.19   3.40               8.50         110     5500    19   
6    mpfi  3.19   3.40               8.50         110     5500    19   
7    mpfi  3.13   3.40               8.30         140     5500    17   
8    mpfi  3.13   3.40               7.00         160     5500    16   
9    mpfi  3.50   2.80               8.80         101     5800    23   
10   mpfi  3.50   2.80               8.80         101     5800    23   
11   mpfi  3.31   3.19               9.00         121     4250    21   
12   mpfi  3.31   3.19               9.00         121     4250    21   
13   mpfi  3.31   3.19               9.00         121     4250    20   
14   mpfi  3.62   3.39               8.00         182     5400    16   
15   mpfi  3.62   3.39               8.00         182     5400    16   
16   mpfi  3.62   3.39               8.00         182     5400    15   
17   2bbl  2.91   3.03               9.50          48     5100    47   
18   2bbl  3.03   3.11               9.60          70     5400    38   
19   2bbl  3.03   3.11               9.60          70     5400    38   
20   2bbl  2.97   3.23               9.41          68     5500    37   
21   2bbl  2.97   3.23               9.40          68     5500    31   
22   mpfi  3.03   3.39               7.60         102     5500    24   

    highway-mpg  price  
0            27  16500  
1            26  16500  
2            30  13950  
3            22  17450  
4            25  15250  
5            25  17710  
6            25  18920  
7            20  23875  
8            22      0  
9            29  16430  
10           29  16925  
11           28  20970  
12           28  21105  
13           25  24565  
14           22  30760  
15           22  41315  
16           20  36880  
17           53   5151  
18           43   6295  
19           43   6575  
20           41   5572  
21           38   6377  
22           30   7957  
>>> df["normalized-losses"].replace(to_replace=0,value=mean_normal,inplace=True)
>>> df.head(24)
    symboling  normalized-losses         make fuel-type aspiration  \
0           3          98.078431  alfa-romero       gas        std   
1           1          98.078431  alfa-romero       gas        std   
2           2         164.000000         audi       gas        std   
3           2         164.000000         audi       gas        std   
4           2          98.078431         audi       gas        std   
5           1         158.000000         audi       gas        std   
6           1          98.078431         audi       gas        std   
7           1         158.000000         audi       gas      turbo   
8           0          98.078431         audi       gas      turbo   
9           2         192.000000          bmw       gas        std   
10          0         192.000000          bmw       gas        std   
11          0         188.000000          bmw       gas        std   
12          0         188.000000          bmw       gas        std   
13          1          98.078431          bmw       gas        std   
14          0          98.078431          bmw       gas        std   
15          0          98.078431          bmw       gas        std   
16          0          98.078431          bmw       gas        std   
17          2         121.000000    chevrolet       gas        std   
18          1          98.000000    chevrolet       gas        std   
19          0          81.000000    chevrolet       gas        std   
20          1         118.000000        dodge       gas        std   
21          1         118.000000        dodge       gas        std   
22          1         118.000000        dodge       gas      turbo   
23          1         148.000000        dodge       gas        std   

   num-of-doors    bodystyle drive-wheels engine-location  wheelbase  length  \
0           two  convertible          rwd           front       88.6   168.8   
1           two    hatchback          rwd           front       94.5   171.2   
2          four        sedan          fwd           front       99.8   176.6   
3          four        sedan          4wd           front       99.4   176.6   
4           two        sedan          fwd           front       99.8   177.3   
5          four        sedan          fwd           front      105.8   192.7   
6          four        wagon          fwd           front      105.8   192.7   
7          four        sedan          fwd           front      105.8   192.7   
8           two    hatchback          4wd           front       99.5   178.2   
9           two        sedan          rwd           front      101.2   176.8   
10         four        sedan          rwd           front      101.2   176.8   
11          two        sedan          rwd           front      101.2   176.8   
12         four        sedan          rwd           front      101.2   176.8   
13         four        sedan          rwd           front      103.5   189.0   
14         four        sedan          rwd           front      103.5   189.0   
15          two        sedan          rwd           front      103.5   193.8   
16         four        sedan          rwd           front      110.0   197.0   
17          two    hatchback          fwd           front       88.4   141.1   
18          two    hatchback          fwd           front       94.5   155.9   
19         four        sedan          fwd           front       94.5   158.8   
20          two    hatchback          fwd           front       93.7   157.3   
21          two    hatchback          fwd           front       93.7   157.3   
22          two    hatchback          fwd           front       93.7   157.3   
23         four    hatchback          fwd           front       93.7   157.3   

    width  height  curved-weight engine-type num-of-cylinder  engine-size  \
0    64.1    48.8           2548        dohc            four          130   
1    65.5    52.4           2823        ohcv             six          152   
2    66.2    54.3           2337         ohc            four          109   
3    66.4    54.3           2824         ohc            five          136   
4    66.3    53.1           2507         ohc            five          136   
5    71.4    55.7           2844         ohc            five          136   
6    71.4    55.7           2954         ohc            five          136   
7    71.4    55.9           3086         ohc            five          131   
8    67.9    52.0           3053         ohc            five          131   
9    64.8    54.3           2395         ohc            four          108   
10   64.8    54.3           2395         ohc            four          108   
11   64.8    54.3           2710         ohc             six          164   
12   64.8    54.3           2765         ohc             six          164   
13   66.9    55.7           3055         ohc             six          164   
14   66.9    55.7           3230         ohc             six          209   
15   67.9    53.7           3380         ohc             six          209   
16   70.9    56.3           3505         ohc             six          209   
17   60.3    53.2           1488           l           three           61   
18   63.6    52.0           1874         ohc            four           90   
19   63.6    52.0           1909         ohc            four           90   
20   63.8    50.8           1876         ohc            four           90   
21   63.8    50.8           1876         ohc            four           90   
22   63.8    50.8           2128         ohc            four           98   
23   63.8    50.6           1967         ohc            four           90   

   system  boar stroke  compression-ratio horse-power peak-rpm  city  \
0    mpfi  3.47   2.68               9.00         111     5000    21   
1    mpfi  2.68   3.47               9.00         154     5000    19   
2    mpfi  3.19   3.40              10.00         102     5500    24   
3    mpfi  3.19   3.40               8.00         115     5500    18   
4    mpfi  3.19   3.40               8.50         110     5500    19   
5    mpfi  3.19   3.40               8.50         110     5500    19   
6    mpfi  3.19   3.40               8.50         110     5500    19   
7    mpfi  3.13   3.40               8.30         140     5500    17   
8    mpfi  3.13   3.40               7.00         160     5500    16   
9    mpfi  3.50   2.80               8.80         101     5800    23   
10   mpfi  3.50   2.80               8.80         101     5800    23   
11   mpfi  3.31   3.19               9.00         121     4250    21   
12   mpfi  3.31   3.19               9.00         121     4250    21   
13   mpfi  3.31   3.19               9.00         121     4250    20   
14   mpfi  3.62   3.39               8.00         182     5400    16   
15   mpfi  3.62   3.39               8.00         182     5400    16   
16   mpfi  3.62   3.39               8.00         182     5400    15   
17   2bbl  2.91   3.03               9.50          48     5100    47   
18   2bbl  3.03   3.11               9.60          70     5400    38   
19   2bbl  3.03   3.11               9.60          70     5400    38   
20   2bbl  2.97   3.23               9.41          68     5500    37   
21   2bbl  2.97   3.23               9.40          68     5500    31   
22   mpfi  3.03   3.39               7.60         102     5500    24   
23   2bbl  2.97   3.23               9.40          68     5500    31   

    highway-mpg  price  
0            27  16500  
1            26  16500  
2            30  13950  
3            22  17450  
4            25  15250  
5            25  17710  
6            25  18920  
7            20  23875  
8            22      0  
9            29  16430  
10           29  16925  
11           28  20970  
12           28  21105  
13           25  24565  
14           22  30760  
15           22  41315  
16           20  36880  
17           53   5151  
18           43   6295  
19           43   6575  
20           41   5572  
21           38   6377  
22           30   7957  
23           38   6229  
>>> df["city"]=235/df["city"]
>>> df.rename(columns={"city":"city_100"},inplace=True)
>>> print(df["city_100"])
0      11.190476
1      12.368421
2       9.791667
3      13.055556
4      12.368421
5      12.368421
6      12.368421
7      13.823529
8      14.687500
9      10.217391
10     10.217391
11     11.190476
12     11.190476
13     11.750000
14     14.687500
15     14.687500
16     15.666667
17      5.000000
18      6.184211
19      6.184211
20      6.351351
21      7.580645
22      9.791667
23      7.580645
24      7.580645
25      7.580645
26      9.791667
27      9.791667
28     12.368421
29      4.795918
         ...    
174     8.703704
175     8.703704
176     8.703704
177    11.750000
178    12.368421
179    11.750000
180    12.368421
181     6.351351
182     8.703704
183     6.351351
184     8.703704
185     8.703704
186     6.351351
187     9.038462
188     9.791667
189     9.791667
190    12.368421
191     7.121212
192     9.400000
193    10.217391
194    10.217391
195     9.791667
196     9.791667
197    13.823529
198    13.823529
199    10.217391
200    12.368421
201    13.055556
202     9.038462
203    12.368421
Name: city_100, Length: 204, dtype: float64
>>> df.head(24)
    symboling  normalized-losses         make fuel-type aspiration  \
0           3          98.078431  alfa-romero       gas        std   
1           1          98.078431  alfa-romero       gas        std   
2           2         164.000000         audi       gas        std   
3           2         164.000000         audi       gas        std   
4           2          98.078431         audi       gas        std   
5           1         158.000000         audi       gas        std   
6           1          98.078431         audi       gas        std   
7           1         158.000000         audi       gas      turbo   
8           0          98.078431         audi       gas      turbo   
9           2         192.000000          bmw       gas        std   
10          0         192.000000          bmw       gas        std   
11          0         188.000000          bmw       gas        std   
12          0         188.000000          bmw       gas        std   
13          1          98.078431          bmw       gas        std   
14          0          98.078431          bmw       gas        std   
15          0          98.078431          bmw       gas        std   
16          0          98.078431          bmw       gas        std   
17          2         121.000000    chevrolet       gas        std   
18          1          98.000000    chevrolet       gas        std   
19          0          81.000000    chevrolet       gas        std   
20          1         118.000000        dodge       gas        std   
21          1         118.000000        dodge       gas        std   
22          1         118.000000        dodge       gas      turbo   
23          1         148.000000        dodge       gas        std   

   num-of-doors    bodystyle drive-wheels engine-location  wheelbase  length  \
0           two  convertible          rwd           front       88.6   168.8   
1           two    hatchback          rwd           front       94.5   171.2   
2          four        sedan          fwd           front       99.8   176.6   
3          four        sedan          4wd           front       99.4   176.6   
4           two        sedan          fwd           front       99.8   177.3   
5          four        sedan          fwd           front      105.8   192.7   
6          four        wagon          fwd           front      105.8   192.7   
7          four        sedan          fwd           front      105.8   192.7   
8           two    hatchback          4wd           front       99.5   178.2   
9           two        sedan          rwd           front      101.2   176.8   
10         four        sedan          rwd           front      101.2   176.8   
11          two        sedan          rwd           front      101.2   176.8   
12         four        sedan          rwd           front      101.2   176.8   
13         four        sedan          rwd           front      103.5   189.0   
14         four        sedan          rwd           front      103.5   189.0   
15          two        sedan          rwd           front      103.5   193.8   
16         four        sedan          rwd           front      110.0   197.0   
17          two    hatchback          fwd           front       88.4   141.1   
18          two    hatchback          fwd           front       94.5   155.9   
19         four        sedan          fwd           front       94.5   158.8   
20          two    hatchback          fwd           front       93.7   157.3   
21          two    hatchback          fwd           front       93.7   157.3   
22          two    hatchback          fwd           front       93.7   157.3   
23         four    hatchback          fwd           front       93.7   157.3   

    width  height  curved-weight engine-type num-of-cylinder  engine-size  \
0    64.1    48.8           2548        dohc            four          130   
1    65.5    52.4           2823        ohcv             six          152   
2    66.2    54.3           2337         ohc            four          109   
3    66.4    54.3           2824         ohc            five          136   
4    66.3    53.1           2507         ohc            five          136   
5    71.4    55.7           2844         ohc            five          136   
6    71.4    55.7           2954         ohc            five          136   
7    71.4    55.9           3086         ohc            five          131   
8    67.9    52.0           3053         ohc            five          131   
9    64.8    54.3           2395         ohc            four          108   
10   64.8    54.3           2395         ohc            four          108   
11   64.8    54.3           2710         ohc             six          164   
12   64.8    54.3           2765         ohc             six          164   
13   66.9    55.7           3055         ohc             six          164   
14   66.9    55.7           3230         ohc             six          209   
15   67.9    53.7           3380         ohc             six          209   
16   70.9    56.3           3505         ohc             six          209   
17   60.3    53.2           1488           l           three           61   
18   63.6    52.0           1874         ohc            four           90   
19   63.6    52.0           1909         ohc            four           90   
20   63.8    50.8           1876         ohc            four           90   
21   63.8    50.8           1876         ohc            four           90   
22   63.8    50.8           2128         ohc            four           98   
23   63.8    50.6           1967         ohc            four           90   

   system  boar stroke  compression-ratio horse-power peak-rpm   city_100  \
0    mpfi  3.47   2.68               9.00         111     5000  11.190476   
1    mpfi  2.68   3.47               9.00         154     5000  12.368421   
2    mpfi  3.19   3.40              10.00         102     5500   9.791667   
3    mpfi  3.19   3.40               8.00         115     5500  13.055556   
4    mpfi  3.19   3.40               8.50         110     5500  12.368421   
5    mpfi  3.19   3.40               8.50         110     5500  12.368421   
6    mpfi  3.19   3.40               8.50         110     5500  12.368421   
7    mpfi  3.13   3.40               8.30         140     5500  13.823529   
8    mpfi  3.13   3.40               7.00         160     5500  14.687500   
9    mpfi  3.50   2.80               8.80         101     5800  10.217391   
10   mpfi  3.50   2.80               8.80         101     5800  10.217391   
11   mpfi  3.31   3.19               9.00         121     4250  11.190476   
12   mpfi  3.31   3.19               9.00         121     4250  11.190476   
13   mpfi  3.31   3.19               9.00         121     4250  11.750000   
14   mpfi  3.62   3.39               8.00         182     5400  14.687500   
15   mpfi  3.62   3.39               8.00         182     5400  14.687500   
16   mpfi  3.62   3.39               8.00         182     5400  15.666667   
17   2bbl  2.91   3.03               9.50          48     5100   5.000000   
18   2bbl  3.03   3.11               9.60          70     5400   6.184211   
19   2bbl  3.03   3.11               9.60          70     5400   6.184211   
20   2bbl  2.97   3.23               9.41          68     5500   6.351351   
21   2bbl  2.97   3.23               9.40          68     5500   7.580645   
22   mpfi  3.03   3.39               7.60         102     5500   9.791667   
23   2bbl  2.97   3.23               9.40          68     5500   7.580645   

    highway-mpg  price  
0            27  16500  
1            26  16500  
2            30  13950  
3            22  17450  
4            25  15250  
5            25  17710  
6            25  18920  
7            20  23875  
8            22      0  
9            29  16430  
10           29  16925  
11           28  20970  
12           28  21105  
13           25  24565  
14           22  30760  
15           22  41315  
16           20  36880  
17           53   5151  
18           43   6295  
19           43   6575  
20           41   5572  
21           38   6377  
22           30   7957  
23           38   6229  
>>> df.dtypes
symboling              int64
normalized-losses    float64
make                  object
fuel-type             object
aspiration            object
num-of-doors          object
bodystyle             object
drive-wheels          object
engine-location       object
wheelbase            float64
length               float64
width                float64
height               float64
curved-weight          int64
engine-type           object
num-of-cylinder       object
engine-size            int64
system                object
boar                  object
stroke                object
compression-ratio    float64
horse-power           object
peak-rpm              object
city_100             float64
highway-mpg            int64
price                 object
dtype: object
>>> df=df.astype({"price":float})
>>> df.dtypes
symboling              int64
normalized-losses    float64
make                  object
fuel-type             object
aspiration            object
num-of-doors          object
bodystyle             object
drive-wheels          object
engine-location       object
wheelbase            float64
length               float64
width                float64
height               float64
curved-weight          int64
engine-type           object
num-of-cylinder       object
engine-size            int64
system                object
boar                  object
stroke                object
compression-ratio    float64
horse-power           object
peak-rpm              object
city_100             float64
highway-mpg            int64
price                float64
dtype: object
>>> df["length"]=(df["length"]-df["length"].mean())/(df["length"].std()) #Simple Features Scaling
>>> df.head(23)
    symboling  normalized-losses         make fuel-type aspiration  \
0           3          98.078431  alfa-romero       gas        std   
1           1          98.078431  alfa-romero       gas        std   
2           2         164.000000         audi       gas        std   
3           2         164.000000         audi       gas        std   
4           2          98.078431         audi       gas        std   
5           1         158.000000         audi       gas        std   
6           1          98.078431         audi       gas        std   
7           1         158.000000         audi       gas      turbo   
8           0          98.078431         audi       gas      turbo   
9           2         192.000000          bmw       gas        std   
10          0         192.000000          bmw       gas        std   
11          0         188.000000          bmw       gas        std   
12          0         188.000000          bmw       gas        std   
13          1          98.078431          bmw       gas        std   
14          0          98.078431          bmw       gas        std   
15          0          98.078431          bmw       gas        std   
16          0          98.078431          bmw       gas        std   
17          2         121.000000    chevrolet       gas        std   
18          1          98.000000    chevrolet       gas        std   
19          0          81.000000    chevrolet       gas        std   
20          1         118.000000        dodge       gas        std   
21          1         118.000000        dodge       gas        std   
22          1         118.000000        dodge       gas      turbo   

   num-of-doors    bodystyle drive-wheels engine-location  wheelbase  \
0           two  convertible          rwd           front       88.6   
1           two    hatchback          rwd           front       94.5   
2          four        sedan          fwd           front       99.8   
3          four        sedan          4wd           front       99.4   
4           two        sedan          fwd           front       99.8   
5          four        sedan          fwd           front      105.8   
6          four        wagon          fwd           front      105.8   
7          four        sedan          fwd           front      105.8   
8           two    hatchback          4wd           front       99.5   
9           two        sedan          rwd           front      101.2   
10         four        sedan          rwd           front      101.2   
11          two        sedan          rwd           front      101.2   
12         four        sedan          rwd           front      101.2   
13         four        sedan          rwd           front      103.5   
14         four        sedan          rwd           front      103.5   
15          two        sedan          rwd           front      103.5   
16         four        sedan          rwd           front      110.0   
17          two    hatchback          fwd           front       88.4   
18          two    hatchback          fwd           front       94.5   
19         four        sedan          fwd           front       94.5   
20          two    hatchback          fwd           front       93.7   
21          two    hatchback          fwd           front       93.7   
22          two    hatchback          fwd           front       93.7   

      length  width  height  curved-weight engine-type num-of-cylinder  \
0  -0.426707   64.1    48.8           2548        dohc            four   
1  -0.232565   65.5    52.4           2823        ohcv             six   
2   0.204253   66.2    54.3           2337         ohc            four   
3   0.204253   66.4    54.3           2824         ohc            five   
4   0.260878   66.3    53.1           2507         ohc            five   
5   1.506618   71.4    55.7           2844         ohc            five   
6   1.506618   71.4    55.7           2954         ohc            five   
7   1.506618   71.4    55.9           3086         ohc            five   
8   0.333681   67.9    52.0           3053         ohc            five   
9   0.220431   64.8    54.3           2395         ohc            four   
10  0.220431   64.8    54.3           2395         ohc            four   
11  0.220431   64.8    54.3           2710         ohc             six   
12  0.220431   64.8    54.3           2765         ohc             six   
13  1.207317   66.9    55.7           3055         ohc             six   
14  1.207317   66.9    55.7           3230         ohc             six   
15  1.595600   67.9    53.7           3380         ohc             six   
16  1.854455   70.9    56.3           3505         ohc             six   
17 -2.667422   60.3    53.2           1488           l           three   
18 -1.470217   63.6    52.0           1874         ohc            four   
19 -1.235629   63.6    52.0           1909         ohc            four   
20 -1.356968   63.8    50.8           1876         ohc            four   
21 -1.356968   63.8    50.8           1876         ohc            four   
22 -1.356968   63.8    50.8           2128         ohc            four   

    engine-size system  boar stroke  compression-ratio horse-power peak-rpm  \
0           130   mpfi  3.47   2.68               9.00         111     5000   
1           152   mpfi  2.68   3.47               9.00         154     5000   
2           109   mpfi  3.19   3.40              10.00         102     5500   
3           136   mpfi  3.19   3.40               8.00         115     5500   
4           136   mpfi  3.19   3.40               8.50         110     5500   
5           136   mpfi  3.19   3.40               8.50         110     5500   
6           136   mpfi  3.19   3.40               8.50         110     5500   
7           131   mpfi  3.13   3.40               8.30         140     5500   
8           131   mpfi  3.13   3.40               7.00         160     5500   
9           108   mpfi  3.50   2.80               8.80         101     5800   
10          108   mpfi  3.50   2.80               8.80         101     5800   
11          164   mpfi  3.31   3.19               9.00         121     4250   
12          164   mpfi  3.31   3.19               9.00         121     4250   
13          164   mpfi  3.31   3.19               9.00         121     4250   
14          209   mpfi  3.62   3.39               8.00         182     5400   
15          209   mpfi  3.62   3.39               8.00         182     5400   
16          209   mpfi  3.62   3.39               8.00         182     5400   
17           61   2bbl  2.91   3.03               9.50          48     5100   
18           90   2bbl  3.03   3.11               9.60          70     5400   
19           90   2bbl  3.03   3.11               9.60          70     5400   
20           90   2bbl  2.97   3.23               9.41          68     5500   
21           90   2bbl  2.97   3.23               9.40          68     5500   
22           98   mpfi  3.03   3.39               7.60         102     5500   

     city_100  highway-mpg    price  
0   11.190476           27  16500.0  
1   12.368421           26  16500.0  
2    9.791667           30  13950.0  
3   13.055556           22  17450.0  
4   12.368421           25  15250.0  
5   12.368421           25  17710.0  
6   12.368421           25  18920.0  
7   13.823529           20  23875.0  
8   14.687500           22      0.0  
9   10.217391           29  16430.0  
10  10.217391           29  16925.0  
11  11.190476           28  20970.0  
12  11.190476           28  21105.0  
13  11.750000           25  24565.0  
14  14.687500           22  30760.0  
15  14.687500           22  41315.0  
16  15.666667           20  36880.0  
17   5.000000           53   5151.0  
18   6.184211           43   6295.0  
19   6.184211           43   6575.0  
20   6.351351           41   5572.0  
21   7.580645           38   6377.0  
22   9.791667           30   7957.0  
>>> #Min-Max Scaling
>>> df["length"]=(df["length"]-df["length"].min())/(df["length"].max()-df["length"].min())
>>> df.head()
   symboling  normalized-losses         make fuel-type aspiration  \
0          3          98.078431  alfa-romero       gas        std   
1          1          98.078431  alfa-romero       gas        std   
2          2         164.000000         audi       gas        std   
3          2         164.000000         audi       gas        std   
4          2          98.078431         audi       gas        std   

  num-of-doors    bodystyle drive-wheels engine-location  wheelbase    length  \
0          two  convertible          rwd           front       88.6  0.413433   
1          two    hatchback          rwd           front       94.5  0.449254   
2         four        sedan          fwd           front       99.8  0.529851   
3         four        sedan          4wd           front       99.4  0.529851   
4          two        sedan          fwd           front       99.8  0.540299   

   width  height  curved-weight engine-type num-of-cylinder  engine-size  \
0   64.1    48.8           2548        dohc            four          130   
1   65.5    52.4           2823        ohcv             six          152   
2   66.2    54.3           2337         ohc            four          109   
3   66.4    54.3           2824         ohc            five          136   
4   66.3    53.1           2507         ohc            five          136   

  system  boar stroke  compression-ratio horse-power peak-rpm   city_100  \
0   mpfi  3.47   2.68                9.0         111     5000  11.190476   
1   mpfi  2.68   3.47                9.0         154     5000  12.368421   
2   mpfi  3.19   3.40               10.0         102     5500   9.791667   
3   mpfi  3.19   3.40                8.0         115     5500  13.055556   
4   mpfi  3.19   3.40                8.5         110     5500  12.368421   

   highway-mpg    price  
0           27  16500.0  
1           26  16500.0  
2           30  13950.0  
3           22  17450.0  
4           25  15250.0  
>>> #Z-scores
>>> df["length"]=(df["length"]-df["length"].mean())/(df["length"].std())
>>> df.head(23)
    symboling  normalized-losses         make fuel-type aspiration  \
0           3          98.078431  alfa-romero       gas        std   
1           1          98.078431  alfa-romero       gas        std   
2           2         164.000000         audi       gas        std   
3           2         164.000000         audi       gas        std   
4           2          98.078431         audi       gas        std   
5           1         158.000000         audi       gas        std   
6           1          98.078431         audi       gas        std   
7           1         158.000000         audi       gas      turbo   
8           0          98.078431         audi       gas      turbo   
9           2         192.000000          bmw       gas        std   
10          0         192.000000          bmw       gas        std   
11          0         188.000000          bmw       gas        std   
12          0         188.000000          bmw       gas        std   
13          1          98.078431          bmw       gas        std   
14          0          98.078431          bmw       gas        std   
15          0          98.078431          bmw       gas        std   
16          0          98.078431          bmw       gas        std   
17          2         121.000000    chevrolet       gas        std   
18          1          98.000000    chevrolet       gas        std   
19          0          81.000000    chevrolet       gas        std   
20          1         118.000000        dodge       gas        std   
21          1         118.000000        dodge       gas        std   
22          1         118.000000        dodge       gas      turbo   

   num-of-doors    bodystyle drive-wheels engine-location  wheelbase  \
0           two  convertible          rwd           front       88.6   
1           two    hatchback          rwd           front       94.5   
2          four        sedan          fwd           front       99.8   
3          four        sedan          4wd           front       99.4   
4           two        sedan          fwd           front       99.8   
5          four        sedan          fwd           front      105.8   
6          four        wagon          fwd           front      105.8   
7          four        sedan          fwd           front      105.8   
8           two    hatchback          4wd           front       99.5   
9           two        sedan          rwd           front      101.2   
10         four        sedan          rwd           front      101.2   
11          two        sedan          rwd           front      101.2   
12         four        sedan          rwd           front      101.2   
13         four        sedan          rwd           front      103.5   
14         four        sedan          rwd           front      103.5   
15          two        sedan          rwd           front      103.5   
16         four        sedan          rwd           front      110.0   
17          two    hatchback          fwd           front       88.4   
18          two    hatchback          fwd           front       94.5   
19         four        sedan          fwd           front       94.5   
20          two    hatchback          fwd           front       93.7   
21          two    hatchback          fwd           front       93.7   
22          two    hatchback          fwd           front       93.7   

      length  width  height  curved-weight engine-type num-of-cylinder  \
0  -0.426707   64.1    48.8           2548        dohc            four   
1  -0.232565   65.5    52.4           2823        ohcv             six   
2   0.204253   66.2    54.3           2337         ohc            four   
3   0.204253   66.4    54.3           2824         ohc            five   
4   0.260878   66.3    53.1           2507         ohc            five   
5   1.506618   71.4    55.7           2844         ohc            five   
6   1.506618   71.4    55.7           2954         ohc            five   
7   1.506618   71.4    55.9           3086         ohc            five   
8   0.333681   67.9    52.0           3053         ohc            five   
9   0.220431   64.8    54.3           2395         ohc            four   
10  0.220431   64.8    54.3           2395         ohc            four   
11  0.220431   64.8    54.3           2710         ohc             six   
12  0.220431   64.8    54.3           2765         ohc             six   
13  1.207317   66.9    55.7           3055         ohc             six   
14  1.207317   66.9    55.7           3230         ohc             six   
15  1.595600   67.9    53.7           3380         ohc             six   
16  1.854455   70.9    56.3           3505         ohc             six   
17 -2.667422   60.3    53.2           1488           l           three   
18 -1.470217   63.6    52.0           1874         ohc            four   
19 -1.235629   63.6    52.0           1909         ohc            four   
20 -1.356968   63.8    50.8           1876         ohc            four   
21 -1.356968   63.8    50.8           1876         ohc            four   
22 -1.356968   63.8    50.8           2128         ohc            four   

    engine-size system  boar stroke  compression-ratio horse-power peak-rpm  \
0           130   mpfi  3.47   2.68               9.00         111     5000   
1           152   mpfi  2.68   3.47               9.00         154     5000   
2           109   mpfi  3.19   3.40              10.00         102     5500   
3           136   mpfi  3.19   3.40               8.00         115     5500   
4           136   mpfi  3.19   3.40               8.50         110     5500   
5           136   mpfi  3.19   3.40               8.50         110     5500   
6           136   mpfi  3.19   3.40               8.50         110     5500   
7           131   mpfi  3.13   3.40               8.30         140     5500   
8           131   mpfi  3.13   3.40               7.00         160     5500   
9           108   mpfi  3.50   2.80               8.80         101     5800   
10          108   mpfi  3.50   2.80               8.80         101     5800   
11          164   mpfi  3.31   3.19               9.00         121     4250   
12          164   mpfi  3.31   3.19               9.00         121     4250   
13          164   mpfi  3.31   3.19               9.00         121     4250   
14          209   mpfi  3.62   3.39               8.00         182     5400   
15          209   mpfi  3.62   3.39               8.00         182     5400   
16          209   mpfi  3.62   3.39               8.00         182     5400   
17           61   2bbl  2.91   3.03               9.50          48     5100   
18           90   2bbl  3.03   3.11               9.60          70     5400   
19           90   2bbl  3.03   3.11               9.60          70     5400   
20           90   2bbl  2.97   3.23               9.41          68     5500   
21           90   2bbl  2.97   3.23               9.40          68     5500   
22           98   mpfi  3.03   3.39               7.60         102     5500   

     city_100  highway-mpg    price  
0   11.190476           27  16500.0  
1   12.368421           26  16500.0  
2    9.791667           30  13950.0  
3   13.055556           22  17450.0  
4   12.368421           25  15250.0  
5   12.368421           25  17710.0  
6   12.368421           25  18920.0  
7   13.823529           20  23875.0  
8   14.687500           22      0.0  
9   10.217391           29  16430.0  
10  10.217391           29  16925.0  
11  11.190476           28  20970.0  
12  11.190476           28  21105.0  
13  11.750000           25  24565.0  
14  14.687500           22  30760.0  
15  14.687500           22  41315.0  
16  15.666667           20  36880.0  
17   5.000000           53   5151.0  
18   6.184211           43   6295.0  
19   6.184211           43   6575.0  
20   6.351351           41   5572.0  
21   7.580645           38   6377.0  
22   9.791667           30   7957.0  
>>> #BINNING
>>> import numpy as np
>>> bins=np.linspace(min(df["price"]), max(df["price"]), 4) #Binning the price column into 3 groups as follows
>>> group_names = ["Low", "Medium", "High"]
>>> df["price-binned"] = pd.cut(df["price"], bins, labels=group_names, include_lowest = 2)
>>> df.head(23)
    symboling  normalized-losses         make fuel-type aspiration  \
0           3          98.078431  alfa-romero       gas        std   
1           1          98.078431  alfa-romero       gas        std   
2           2         164.000000         audi       gas        std   
3           2         164.000000         audi       gas        std   
4           2          98.078431         audi       gas        std   
5           1         158.000000         audi       gas        std   
6           1          98.078431         audi       gas        std   
7           1         158.000000         audi       gas      turbo   
8           0          98.078431         audi       gas      turbo   
9           2         192.000000          bmw       gas        std   
10          0         192.000000          bmw       gas        std   
11          0         188.000000          bmw       gas        std   
12          0         188.000000          bmw       gas        std   
13          1          98.078431          bmw       gas        std   
14          0          98.078431          bmw       gas        std   
15          0          98.078431          bmw       gas        std   
16          0          98.078431          bmw       gas        std   
17          2         121.000000    chevrolet       gas        std   
18          1          98.000000    chevrolet       gas        std   
19          0          81.000000    chevrolet       gas        std   
20          1         118.000000        dodge       gas        std   
21          1         118.000000        dodge       gas        std   
22          1         118.000000        dodge       gas      turbo   

   num-of-doors    bodystyle drive-wheels engine-location  wheelbase  \
0           two  convertible          rwd           front       88.6   
1           two    hatchback          rwd           front       94.5   
2          four        sedan          fwd           front       99.8   
3          four        sedan          4wd           front       99.4   
4           two        sedan          fwd           front       99.8   
5          four        sedan          fwd           front      105.8   
6          four        wagon          fwd           front      105.8   
7          four        sedan          fwd           front      105.8   
8           two    hatchback          4wd           front       99.5   
9           two        sedan          rwd           front      101.2   
10         four        sedan          rwd           front      101.2   
11          two        sedan          rwd           front      101.2   
12         four        sedan          rwd           front      101.2   
13         four        sedan          rwd           front      103.5   
14         four        sedan          rwd           front      103.5   
15          two        sedan          rwd           front      103.5   
16         four        sedan          rwd           front      110.0   
17          two    hatchback          fwd           front       88.4   
18          two    hatchback          fwd           front       94.5   
19         four        sedan          fwd           front       94.5   
20          two    hatchback          fwd           front       93.7   
21          two    hatchback          fwd           front       93.7   
22          two    hatchback          fwd           front       93.7   

      length  width  height  ...  engine-type num-of-cylinder engine-size  \
0  -0.426707   64.1    48.8  ...         dohc            four         130   
1  -0.232565   65.5    52.4  ...         ohcv             six         152   
2   0.204253   66.2    54.3  ...          ohc            four         109   
3   0.204253   66.4    54.3  ...          ohc            five         136   
4   0.260878   66.3    53.1  ...          ohc            five         136   
5   1.506618   71.4    55.7  ...          ohc            five         136   
6   1.506618   71.4    55.7  ...          ohc            five         136   
7   1.506618   71.4    55.9  ...          ohc            five         131   
8   0.333681   67.9    52.0  ...          ohc            five         131   
9   0.220431   64.8    54.3  ...          ohc            four         108   
10  0.220431   64.8    54.3  ...          ohc            four         108   
11  0.220431   64.8    54.3  ...          ohc             six         164   
12  0.220431   64.8    54.3  ...          ohc             six         164   
13  1.207317   66.9    55.7  ...          ohc             six         164   
14  1.207317   66.9    55.7  ...          ohc             six         209   
15  1.595600   67.9    53.7  ...          ohc             six         209   
16  1.854455   70.9    56.3  ...          ohc             six         209   
17 -2.667422   60.3    53.2  ...            l           three          61   
18 -1.470217   63.6    52.0  ...          ohc            four          90   
19 -1.235629   63.6    52.0  ...          ohc            four          90   
20 -1.356968   63.8    50.8  ...          ohc            four          90   
21 -1.356968   63.8    50.8  ...          ohc            four          90   
22 -1.356968   63.8    50.8  ...          ohc            four          98   

    system  boar stroke compression-ratio  horse-power peak-rpm   city_100  \
0     mpfi  3.47   2.68              9.00          111     5000  11.190476   
1     mpfi  2.68   3.47              9.00          154     5000  12.368421   
2     mpfi  3.19   3.40             10.00          102     5500   9.791667   
3     mpfi  3.19   3.40              8.00          115     5500  13.055556   
4     mpfi  3.19   3.40              8.50          110     5500  12.368421   
5     mpfi  3.19   3.40              8.50          110     5500  12.368421   
6     mpfi  3.19   3.40              8.50          110     5500  12.368421   
7     mpfi  3.13   3.40              8.30          140     5500  13.823529   
8     mpfi  3.13   3.40              7.00          160     5500  14.687500   
9     mpfi  3.50   2.80              8.80          101     5800  10.217391   
10    mpfi  3.50   2.80              8.80          101     5800  10.217391   
11    mpfi  3.31   3.19              9.00          121     4250  11.190476   
12    mpfi  3.31   3.19              9.00          121     4250  11.190476   
13    mpfi  3.31   3.19              9.00          121     4250  11.750000   
14    mpfi  3.62   3.39              8.00          182     5400  14.687500   
15    mpfi  3.62   3.39              8.00          182     5400  14.687500   
16    mpfi  3.62   3.39              8.00          182     5400  15.666667   
17    2bbl  2.91   3.03              9.50           48     5100   5.000000   
18    2bbl  3.03   3.11              9.60           70     5400   6.184211   
19    2bbl  3.03   3.11              9.60           70     5400   6.184211   
20    2bbl  2.97   3.23              9.41           68     5500   6.351351   
21    2bbl  2.97   3.23              9.40           68     5500   7.580645   
22    mpfi  3.03   3.39              7.60          102     5500   9.791667   

    highway-mpg    price  price-binned  
0            27  16500.0        Medium  
1            26  16500.0        Medium  
2            30  13950.0           Low  
3            22  17450.0        Medium  
4            25  15250.0        Medium  
5            25  17710.0        Medium  
6            25  18920.0        Medium  
7            20  23875.0        Medium  
8            22      0.0           Low  
9            29  16430.0        Medium  
10           29  16925.0        Medium  
11           28  20970.0        Medium  
12           28  21105.0        Medium  
13           25  24565.0        Medium  
14           22  30760.0          High  
15           22  41315.0          High  
16           20  36880.0          High  
17           53   5151.0           Low  
18           43   6295.0           Low  
19           43   6575.0           Low  
20           41   5572.0           Low  
21           38   6377.0           Low  
22           30   7957.0           Low  

[23 rows x 27 columns]
>>> # Creating Dummies for column fuel-type so as to distinguish the 2 types of fuels.
>>> pd.get_dummies(df["fuel-type"])
     diesel  gas
0         0    1
1         0    1
2         0    1
3         0    1
4         0    1
5         0    1
6         0    1
7         0    1
8         0    1
9         0    1
10        0    1
11        0    1
12        0    1
13        0    1
14        0    1
15        0    1
16        0    1
17        0    1
18        0    1
19        0    1
20        0    1
21        0    1
22        0    1
23        0    1
24        0    1
25        0    1
26        0    1
27        0    1
28        0    1
29        0    1
..      ...  ...
174       0    1
175       0    1
176       0    1
177       0    1
178       0    1
179       0    1
180       0    1
181       1    0
182       0    1
183       1    0
184       0    1
185       0    1
186       1    0
187       0    1
188       0    1
189       0    1
190       0    1
191       1    0
192       0    1
193       0    1
194       0    1
195       0    1
196       0    1
197       0    1
198       0    1
199       0    1
200       0    1
201       0    1
202       1    0
203       0    1

[204 rows x 2 columns]
>>> #Distribution, Counting Different Wheel types
>>> drive_wheels_counts=df["drive-wheels"]
>>> print(drive_wheels_counts)
0      rwd
1      rwd
2      fwd
3      4wd
4      fwd
5      fwd
6      fwd
7      fwd
8      4wd
9      rwd
10     rwd
11     rwd
12     rwd
13     rwd
14     rwd
15     rwd
16     rwd
17     fwd
18     fwd
19     fwd
20     fwd
21     fwd
22     fwd
23     fwd
24     fwd
25     fwd
26     fwd
27     fwd
28     fwd
29     fwd
      ... 
174    fwd
175    fwd
176    fwd
177    rwd
178    rwd
179    rwd
180    rwd
181    fwd
182    fwd
183    fwd
184    fwd
185    fwd
186    fwd
187    fwd
188    fwd
189    fwd
190    fwd
191    fwd
192    fwd
193    rwd
194    rwd
195    rwd
196    rwd
197    rwd
198    rwd
199    rwd
200    rwd
201    rwd
202    rwd
203    rwd
Name: drive-wheels, Length: 204, dtype: object
>>> dwc=df["drive-wheels"].value_counts()
>>> print(dwc)
fwd    120
rwd     75
4wd      9
Name: drive-wheels, dtype: int64
>>> #VISUALIZATION.
>>> import seaborn as sns
>>> import matplotlib.pyplot as plt
>>> #Box Plot.
>>> sns.boxplot(x="drive-wheels", y="price", data =df)
<matplotlib.axes._subplots.AxesSubplot object at 0x000001A237618DD8>
>>> plt.show() #Displaying the plot.
>>> plt.close('all')
>>> #Scatter Plot.
>>> y=df["engine-size"]
>>> x=df["price"]
>>> plt.scatter(x,y)
<matplotlib.collections.PathCollection object at 0x000001A23A953C88>
>>> plt.show()
>>> plt.close('all')
>>> #Group-by operation
>>> df_new=df[['drive-wheels','bodystyle','price']]
>>> group=df_new.groupby(['drive-wheels','bodystyle'],as_index=False).mean()
>>> df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 204 entries, 0 to 203
Data columns (total 27 columns):
symboling            204 non-null int64
normalized-losses    204 non-null float64
make                 204 non-null object
fuel-type            204 non-null object
aspiration           204 non-null object
num-of-doors         204 non-null object
bodystyle            204 non-null object
drive-wheels         204 non-null object
engine-location      204 non-null object
wheelbase            204 non-null float64
length               204 non-null float64
width                204 non-null float64
height               204 non-null float64
curved-weight        204 non-null int64
engine-type          204 non-null object
num-of-cylinder      204 non-null object
engine-size          204 non-null int64
system               204 non-null object
boar                 204 non-null object
stroke               204 non-null object
compression-ratio    204 non-null float64
horse-power          204 non-null object
peak-rpm             204 non-null object
city_100             204 non-null float64
highway-mpg          204 non-null int64
price                204 non-null float64
price-binned         204 non-null category
dtypes: category(1), float64(8), int64(4), object(14)
memory usage: 41.8+ KB
>>> group
   drive-wheels    bodystyle         price
0           4wd    hatchback   3801.500000
1           4wd        sedan  12647.333333
2           4wd        wagon   9095.750000
3           fwd  convertible  11595.000000
4           fwd      hardtop   8249.000000
5           fwd    hatchback   8396.387755
6           fwd        sedan   9467.526316
7           fwd        wagon   9997.333333
8           rwd  convertible  26563.250000
9           rwd      hardtop  24202.714286
10          rwd    hatchback  13583.157895
11          rwd        sedan  21711.833333
12          rwd        wagon  16994.222222
>>> #PIVOT operation.
>>> df_pivot=group.pivot(index='drive-wheels',columns='bodystyle')
>>> df_pivot
                   price                                            \
bodystyle    convertible       hardtop     hatchback         sedan   
drive-wheels                                                         
4wd                  NaN           NaN   3801.500000  12647.333333   
fwd             11595.00   8249.000000   8396.387755   9467.526316   
rwd             26563.25  24202.714286  13583.157895  21711.833333   

                            
bodystyle            wagon  
drive-wheels                
4wd            9095.750000  
fwd            9997.333333  
rwd           16994.222222  
>>> df.head(20)
    symboling  normalized-losses         make fuel-type aspiration  \
0           3          98.078431  alfa-romero       gas        std   
1           1          98.078431  alfa-romero       gas        std   
2           2         164.000000         audi       gas        std   
3           2         164.000000         audi       gas        std   
4           2          98.078431         audi       gas        std   
5           1         158.000000         audi       gas        std   
6           1          98.078431         audi       gas        std   
7           1         158.000000         audi       gas      turbo   
8           0          98.078431         audi       gas      turbo   
9           2         192.000000          bmw       gas        std   
10          0         192.000000          bmw       gas        std   
11          0         188.000000          bmw       gas        std   
12          0         188.000000          bmw       gas        std   
13          1          98.078431          bmw       gas        std   
14          0          98.078431          bmw       gas        std   
15          0          98.078431          bmw       gas        std   
16          0          98.078431          bmw       gas        std   
17          2         121.000000    chevrolet       gas        std   
18          1          98.000000    chevrolet       gas        std   
19          0          81.000000    chevrolet       gas        std   

   num-of-doors    bodystyle drive-wheels engine-location  wheelbase  \
0           two  convertible          rwd           front       88.6   
1           two    hatchback          rwd           front       94.5   
2          four        sedan          fwd           front       99.8   
3          four        sedan          4wd           front       99.4   
4           two        sedan          fwd           front       99.8   
5          four        sedan          fwd           front      105.8   
6          four        wagon          fwd           front      105.8   
7          four        sedan          fwd           front      105.8   
8           two    hatchback          4wd           front       99.5   
9           two        sedan          rwd           front      101.2   
10         four        sedan          rwd           front      101.2   
11          two        sedan          rwd           front      101.2   
12         four        sedan          rwd           front      101.2   
13         four        sedan          rwd           front      103.5   
14         four        sedan          rwd           front      103.5   
15          two        sedan          rwd           front      103.5   
16         four        sedan          rwd           front      110.0   
17          two    hatchback          fwd           front       88.4   
18          two    hatchback          fwd           front       94.5   
19         four        sedan          fwd           front       94.5   

      length  width  height  ...  engine-type num-of-cylinder engine-size  \
0  -0.426707   64.1    48.8  ...         dohc            four         130   
1  -0.232565   65.5    52.4  ...         ohcv             six         152   
2   0.204253   66.2    54.3  ...          ohc            four         109   
3   0.204253   66.4    54.3  ...          ohc            five         136   
4   0.260878   66.3    53.1  ...          ohc            five         136   
5   1.506618   71.4    55.7  ...          ohc            five         136   
6   1.506618   71.4    55.7  ...          ohc            five         136   
7   1.506618   71.4    55.9  ...          ohc            five         131   
8   0.333681   67.9    52.0  ...          ohc            five         131   
9   0.220431   64.8    54.3  ...          ohc            four         108   
10  0.220431   64.8    54.3  ...          ohc            four         108   
11  0.220431   64.8    54.3  ...          ohc             six         164   
12  0.220431   64.8    54.3  ...          ohc             six         164   
13  1.207317   66.9    55.7  ...          ohc             six         164   
14  1.207317   66.9    55.7  ...          ohc             six         209   
15  1.595600   67.9    53.7  ...          ohc             six         209   
16  1.854455   70.9    56.3  ...          ohc             six         209   
17 -2.667422   60.3    53.2  ...            l           three          61   
18 -1.470217   63.6    52.0  ...          ohc            four          90   
19 -1.235629   63.6    52.0  ...          ohc            four          90   

    system  boar stroke compression-ratio  horse-power peak-rpm   city_100  \
0     mpfi  3.47   2.68               9.0          111     5000  11.190476   
1     mpfi  2.68   3.47               9.0          154     5000  12.368421   
2     mpfi  3.19   3.40              10.0          102     5500   9.791667   
3     mpfi  3.19   3.40               8.0          115     5500  13.055556   
4     mpfi  3.19   3.40               8.5          110     5500  12.368421   
5     mpfi  3.19   3.40               8.5          110     5500  12.368421   
6     mpfi  3.19   3.40               8.5          110     5500  12.368421   
7     mpfi  3.13   3.40               8.3          140     5500  13.823529   
8     mpfi  3.13   3.40               7.0          160     5500  14.687500   
9     mpfi  3.50   2.80               8.8          101     5800  10.217391   
10    mpfi  3.50   2.80               8.8          101     5800  10.217391   
11    mpfi  3.31   3.19               9.0          121     4250  11.190476   
12    mpfi  3.31   3.19               9.0          121     4250  11.190476   
13    mpfi  3.31   3.19               9.0          121     4250  11.750000   
14    mpfi  3.62   3.39               8.0          182     5400  14.687500   
15    mpfi  3.62   3.39               8.0          182     5400  14.687500   
16    mpfi  3.62   3.39               8.0          182     5400  15.666667   
17    2bbl  2.91   3.03               9.5           48     5100   5.000000   
18    2bbl  3.03   3.11               9.6           70     5400   6.184211   
19    2bbl  3.03   3.11               9.6           70     5400   6.184211   

    highway-mpg    price  price-binned  
0            27  16500.0        Medium  
1            26  16500.0        Medium  
2            30  13950.0           Low  
3            22  17450.0        Medium  
4            25  15250.0        Medium  
5            25  17710.0        Medium  
6            25  18920.0        Medium  
7            20  23875.0        Medium  
8            22      0.0           Low  
9            29  16430.0        Medium  
10           29  16925.0        Medium  
11           28  20970.0        Medium  
12           28  21105.0        Medium  
13           25  24565.0        Medium  
14           22  30760.0          High  
15           22  41315.0          High  
16           20  36880.0          High  
17           53   5151.0           Low  
18           43   6295.0           Low  
19           43   6575.0           Low  

[20 rows x 27 columns]
>>> plt.pcolor(df_pivot,cmap='RdBu')
<matplotlib.collections.PolyCollection object at 0x000001A23CBBA390>
>>> plt.colorbar()
<matplotlib.colorbar.Colorbar object at 0x000001A23CBE5EB8>
>>> plt.show()
>>> plt.close('all')
>>> df.groupby(['drive-wheels']).mean()
              symboling  normalized-losses   wheelbase    length      width  \
drive-wheels                                                                  
4wd            0.444444          99.008715   96.822222 -0.215488  65.211111   
fwd            0.941667         112.942484   96.429167 -0.428324  65.057500   
rwd            0.680000         126.492810  102.848000  0.711178  67.376000   

                 height  curved-weight  engine-size  compression-ratio  \
drive-wheels                                                             
4wd           55.400000    2609.111111   110.111111           8.344444   
fwd           53.519167    2264.408333   108.783333           9.933500   
rwd           53.918667    3015.093333   157.880000          10.708000   

               city_100  highway-mpg         price  
drive-wheels                                        
4wd           10.467449    27.222222   9103.111111  
fwd            8.704120    34.225000   9090.700000  
rwd           11.863478    25.666667  19577.680000  
>>> df.groupby(['drive-wheels','bodystyle']).mean()
                          symboling  normalized-losses   wheelbase    length  \
drive-wheels bodystyle                                                         
4wd          hatchback     1.000000          90.539216   96.400000 -0.511644   
             sedan         0.666667         122.666667   97.800000 -0.043817   
             wagon         0.000000          85.500000   96.300000 -0.196164   
fwd          convertible   3.000000          98.078431   94.500000 -1.195183   
             hardtop       2.000000         168.000000   95.100000 -0.944417   
             hatchback     1.367347         119.006403   95.063265 -0.819447   
             sedan         0.701754         111.060888   97.180702 -0.183036   
             wagon         0.083333          93.769608   98.708333  0.110553   
rwd          convertible   2.750000         118.039216   93.275000 -0.042468   
             hardtop       1.857143         112.747899   98.985714  0.399550   
             hatchback     2.210526         152.283798   96.663158 -0.062691   
             sedan        -0.277778         125.744009  106.300000  1.050701   
             wagon        -0.555556          89.488017  109.355556  1.564142   

                              width     height  curved-weight  engine-size  \
drive-wheels bodystyle                                                       
4wd          hatchback    65.850000  53.850000    2646.500000   119.500000   
             sedan        65.733333  54.300000    2573.000000   117.333333   
             wagon        64.500000  57.000000    2617.500000   100.000000   
fwd          convertible  64.200000  55.600000    2254.000000   109.000000   
             hardtop      63.800000  53.300000    2008.000000    97.000000   
             hatchback    64.671429  52.442857    2181.551020   105.816327   
             sedan        65.326316  53.887719    2298.228070   109.947368   
             wagon        65.533333  56.008333    2464.333333   116.333333   
rwd          convertible  66.300000  51.050000    3002.000000   176.000000   
             hardtop      67.014286  52.785714    2925.285714   187.571429   
             hatchback    66.668421  51.063158    2746.526316   136.000000   
             sedan        67.783333  55.052778    3108.305556   165.000000   
             wagon        68.000000  57.566667    3284.888889   144.444444   

                          compression-ratio   city_100  highway-mpg  \
drive-wheels bodystyle                                                
4wd          hatchback             7.850000  11.862981    26.500000   
             sedan                 8.233333  10.879630    25.333333   
             wagon                 8.675000   9.460548    29.000000   
fwd          convertible           8.500000   9.791667    29.000000   
             hardtop               9.400000   7.580645    37.000000   
             hatchback             9.071837   8.524647    34.795918   
             sedan                10.919298   8.695676    34.368421   
             wagon                 8.933333   9.480067    31.416667   
rwd          convertible           9.025000  12.373293    25.000000   
             hardtop              10.914286  12.069942    25.857143   
             hatchback             9.036842  12.034263    26.000000   
             sedan                11.191667  11.852983    25.694444   
             wagon                12.888889  11.157741    25.000000   

                                 price  
drive-wheels bodystyle                  
4wd          hatchback     3801.500000  
             sedan        12647.333333  
             wagon         9095.750000  
fwd          convertible  11595.000000  
             hardtop       8249.000000  
             hatchback     8396.387755  
             sedan         9467.526316  
             wagon         9997.333333  
rwd          convertible  26563.250000  
             hardtop      24202.714286  
             hatchback    13583.157895  
             sedan        21711.833333  
             wagon        16994.222222  
>>> df.groupby(['drive-wheels','bodystyle','price'])
<pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001A23CBFC208>
>>> df.groupby(['drive-wheels','bodystyle','price']).mean()
                                  symboling  normalized-losses  wheelbase  \
drive-wheels bodystyle   price                                              
4wd          hatchback   0.0            0.0          98.078431       99.5   
                         7603.0         2.0          83.000000       93.3   
             sedan       9233.0         0.0         102.000000       97.0   
                         11259.0        0.0         102.000000       97.0   
                         17450.0        2.0         164.000000       99.4   
             wagon       7898.0         0.0          81.000000       95.7   
                         8013.0         0.0          85.000000       96.9   
                         8778.0         0.0          91.000000       95.7   
                         11694.0        0.0          85.000000       96.9   
fwd          convertible 11595.0        3.0          98.078431       94.5   
             hardtop     8249.0         2.0         168.000000       95.1   
             hatchback   5118.0         2.0          83.000000       93.7   
                         5151.0         2.0         121.000000       88.4   
                         5195.0         1.0         104.000000       93.1   
                         5348.0         1.0          87.000000       95.7   
                         5389.0         2.0         161.000000       93.7   
                         5399.0         1.0         101.000000       93.7   
                         5572.0         1.0         118.500000       93.7   
                         6095.0         1.0         104.000000       93.1   
                         6189.0         2.0         161.000000       93.7   
                         6229.0         1.0         151.000000       93.7   
                         6295.0         1.0          98.000000       94.5   
                         6338.0         1.0          87.000000       95.7   
                         6377.0         1.0         118.000000       93.7   
                         6479.0         2.0         137.000000       86.6   
                         6488.0         1.0          74.000000       95.7   
                         6529.0         1.0         101.000000       93.7   
                         6669.0         2.0         161.000000       93.7   
                         6795.0         1.0         104.000000       93.1   
                         6855.0         2.0         137.000000       86.6   
...                                     ...                ...        ...   
rwd          sedan       18150.0        0.0         161.000000      108.0   
                         18280.0        0.0         118.000000      104.9   
                         18344.0        0.0          98.078431      104.9   
                         18420.0       -2.0         103.000000      104.3   
                         19045.0       -1.0          95.000000      109.1   
                         20970.0        0.0         188.000000      101.2   
                         21105.0        0.0         188.000000      101.2   
                         21485.0       -1.0          95.000000      109.1   
                         22470.0       -1.0          95.000000      109.1   
                         22625.0       -1.0          95.000000      109.1   
                         24565.0        1.0          98.078431      103.5   
                         25552.0       -1.0          93.000000      110.0   
                         30760.0        0.0          98.078431      103.5   
                         31600.0       -1.0          93.000000      115.6   
                         32250.0        0.0         145.000000      113.0   
                         34184.0       -1.0          98.078431      115.6   
                         35550.0        0.0          98.078431      113.0   
                         36000.0        0.0          98.078431      102.0   
                         36880.0        0.0          98.078431      110.0   
                         40960.0        0.0          98.078431      120.9   
                         41315.0        0.0          98.078431      103.5   
             wagon       12440.0        0.0          98.078431      114.2   
                         13415.0       -1.0          74.000000      104.3   
                         13860.0        0.0          98.078431      114.2   
                         15750.0       -1.0          98.078431      104.5   
                         16515.0       -1.0          74.000000      104.3   
                         16695.0        0.0          98.078431      114.2   
                         17075.0        0.0          98.078431      114.2   
                         18950.0       -1.0          74.000000      104.3   
                         28248.0       -1.0          93.000000      110.0   

                                    length  width  height  curved-weight  \
drive-wheels bodystyle   price                                             
4wd          hatchback   0.0      0.333681   67.9    52.0         3053.0   
                         7603.0  -1.356968   63.8    55.7         2240.0   
             sedan       9233.0  -0.167851   65.4    54.3         2385.0   
                         11259.0 -0.167851   65.4    54.3         2510.0   
                         17450.0  0.204253   66.4    54.3         2824.0   
             wagon       7898.0  -0.353904   63.6    59.1         2290.0   
                         8013.0  -0.038424   65.4    54.9         2420.0   
                         8778.0  -0.353904   63.6    59.1         3110.0   
                         11694.0 -0.038424   65.4    54.9         2650.0   
fwd          convertible 11595.0 -1.195183   64.2    55.6         2254.0   
             hardtop     8249.0  -0.944417   63.8    53.3         2008.0   
             hatchback   5118.0  -1.389324   63.4    53.7         2050.0   
                         5151.0  -2.667422   60.3    53.2         1488.0   
                         5195.0  -1.211362   64.2    54.1         1890.0   
                         5348.0  -1.243718   63.6    54.5         1985.0   
                         5389.0  -1.356968   64.4    50.8         1918.0   
                         5399.0  -1.947481   64.0    52.6         1837.0   
                         5572.0  -1.356968   63.8    50.8         1897.0   
                         6095.0  -1.211362   64.2    54.1         1900.0   
                         6189.0  -1.356968   64.4    50.8         1944.0   
                         6229.0  -1.356968   63.8    50.6         1967.0   
                         6295.0  -1.470217   63.6    52.0         1874.0   
                         6338.0  -1.243718   63.6    54.5         2040.0   
                         6377.0  -1.356968   63.8    50.8         1876.0   
                         6479.0  -2.384299   63.9    50.8         1713.0   
                         6488.0  -1.243718   63.6    54.5         2015.0   
                         6529.0  -1.947481   64.0    52.6         1940.0   
                         6669.0  -1.356968   64.4    50.8         2004.0   
                         6795.0  -1.211362   64.2    54.1         1905.0   
                         6855.0  -2.384299   63.9    50.8         1819.0   
...                                    ...    ...     ...            ...   
rwd          sedan       18150.0  1.021265   68.3    56.0         3130.0   
                         18280.0  0.074825   66.1    54.4         2670.0   
                         18344.0  0.074825   66.1    54.4         2700.0   
                         18420.0  1.191138   67.2    56.2         3045.0   
                         19045.0  1.191138   68.8    55.5         3049.0   
                         20970.0  0.220431   64.8    54.3         2710.0   
                         21105.0  0.220431   64.8    54.3         2765.0   
                         21485.0  1.191138   68.9    55.5         3012.0   
                         22470.0  1.191138   68.9    55.5         3217.0   
                         22625.0  1.191138   68.9    55.5         3062.0   
                         24565.0  1.207317   66.9    55.7         3055.0   
                         25552.0  1.361012   70.3    56.5         3515.0   
                         30760.0  1.207317   66.9    55.7         3230.0   
                         31600.0  2.307452   71.7    56.3         3770.0   
                         32250.0  2.064775   69.6    52.8         4066.0   
                         34184.0  2.307452   71.7    56.5         3740.0   
                         35550.0  2.064775   69.6    52.8         4066.0   
                         36000.0  1.425726   70.6    47.8         3950.0   
                         36880.0  1.854455   70.9    56.3         3505.0   
                         40960.0  2.752359   71.7    56.7         3900.0   
                         41315.0  1.595600   67.9    53.7         3380.0   
             wagon       12440.0  2.008150   68.4    58.7         3230.0   
                         13415.0  1.191138   67.2    57.5         3034.0   
                         13860.0  2.008150   68.4    58.7         3430.0   
                         15750.0  1.110246   66.5    54.1         3151.0   
                         16515.0  1.191138   67.2    57.5         3042.0   
                         16695.0  2.008150   68.4    56.7         3285.0   
                         17075.0  2.008150   68.4    58.7         3485.0   
                         18950.0  1.191138   67.2    57.5         3157.0   
                         28248.0  1.361012   70.3    58.7         3750.0   

                                  engine-size  compression-ratio   city_100  \
drive-wheels bodystyle   price                                                
4wd          hatchback   0.0            131.0              7.000  14.687500   
                         7603.0         108.0              8.700   9.038462   
             sedan       9233.0         108.0              9.000   9.791667   
                         11259.0        108.0              7.700   9.791667   
                         17450.0        136.0              8.000  13.055556   
             wagon       7898.0          92.0              9.000   8.703704   
                         8013.0         108.0              9.000  10.217391   
                         8778.0          92.0              9.000   8.703704   
                         11694.0        108.0              7.700  10.217391   
fwd          convertible 11595.0        109.0              8.500   9.791667   
             hardtop     8249.0          97.0              9.400   7.580645   
             hatchback   5118.0          97.0              9.000   7.580645   
                         5151.0          61.0              9.500   5.000000   
                         5195.0          91.0              9.000   7.833333   
                         5348.0          92.0              9.000   6.714286   
                         5389.0          92.0              9.400   6.351351   
                         5399.0          79.0             10.100   6.184211   
                         5572.0          90.0              9.405   6.351351   
                         6095.0          91.0              9.000   7.580645   
                         6189.0          92.0              9.400   7.580645   
                         6229.0          90.0              9.400   7.580645   
                         6295.0          90.0              9.600   6.184211   
                         6338.0          92.0              9.000   7.580645   
                         6377.0          90.0              9.400   7.580645   
                         6479.0          92.0              9.600   4.795918   
                         6488.0          92.0              9.000   7.580645   
                         6529.0          92.0              9.200   7.833333   
                         6669.0          92.0              9.400   7.580645   
                         6795.0          91.0              9.000   7.580645   
                         6855.0          92.0              9.200   7.580645   
...                                       ...                ...        ...   
rwd          sedan       18150.0        134.0              7.000  13.055556   
                         18280.0        140.0              8.000  12.368421   
                         18344.0        134.0             22.000   7.580645   
                         18420.0        130.0              7.500  13.823529   
                         19045.0        141.0              8.700  12.368421   
                         20970.0        164.0              9.000  11.190476   
                         21105.0        164.0              9.000  11.190476   
                         21485.0        173.0              8.800  13.055556   
                         22470.0        145.0             23.000   9.038462   
                         22625.0        141.0              9.500  12.368421   
                         24565.0        164.0              9.000  11.750000   
                         25552.0        183.0             21.500  10.681818   
                         30760.0        209.0              8.000  14.687500   
                         31600.0        183.0             21.500  10.681818   
                         32250.0        258.0              8.100  15.666667   
                         34184.0        234.0              8.300  14.687500   
                         35550.0        258.0              8.100  15.666667   
                         36000.0        326.0             11.500  18.076923   
                         36880.0        209.0              8.000  15.666667   
                         40960.0        308.0              8.000  16.785714   
                         41315.0        209.0              8.000  14.687500   
             wagon       12440.0        120.0              8.400  12.368421   
                         13415.0        141.0              9.500  10.217391   
                         13860.0        152.0             21.000   9.400000   
                         15750.0        161.0              9.200  12.368421   
                         16515.0        141.0              9.500   9.791667   
                         16695.0        120.0              8.400  12.368421   
                         17075.0        152.0             21.000   9.400000   
                         18950.0        130.0              7.500  13.823529   
                         28248.0        183.0             21.500  10.681818   

                                  highway-mpg  
drive-wheels bodystyle   price                 
4wd          hatchback   0.0             22.0  
                         7603.0          31.0  
             sedan       9233.0          25.0  
                         11259.0         29.0  
                         17450.0         22.0  
             wagon       7898.0          32.0  
                         8013.0          29.0  
                         8778.0          32.0  
                         11694.0         23.0  
fwd          convertible 11595.0         29.0  
             hardtop     8249.0          37.0  
             hatchback   5118.0          36.0  
                         5151.0          53.0  
                         5195.0          31.0  
                         5348.0          39.0  
                         5389.0          41.0  
                         5399.0          42.0  
                         5572.0          41.0  
                         6095.0          38.0  
                         6189.0          38.0  
                         6229.0          38.0  
                         6295.0          43.0  
                         6338.0          38.0  
                         6377.0          38.0  
                         6479.0          54.0  
                         6488.0          38.0  
                         6529.0          34.0  
                         6669.0          38.0  
                         6795.0          38.0  
                         6855.0          38.0  
...                                       ...  
rwd          sedan       18150.0         24.0  
                         18280.0         27.0  
                         18344.0         39.0  
                         18420.0         22.0  
                         19045.0         25.0  
                         20970.0         28.0  
                         21105.0         28.0  
                         21485.0         23.0  
                         22470.0         27.0  
                         22625.0         25.0  
                         24565.0         25.0  
                         25552.0         25.0  
                         30760.0         22.0  
                         31600.0         25.0  
                         32250.0         19.0  
                         34184.0         18.0  
                         35550.0         19.0  
                         36000.0         17.0  
                         36880.0         20.0  
                         40960.0         16.0  
                         41315.0         22.0  
             wagon       12440.0         24.0  
                         13415.0         28.0  
                         13860.0         25.0  
                         15750.0         24.0  
                         16515.0         28.0  
                         16695.0         24.0  
                         17075.0         25.0  
                         18950.0         22.0  
                         28248.0         25.0  

[193 rows x 11 columns]
>>> #ANOVA (Analysis Of Variance)
>>> df_anova=df[["make","price"]]
>>> group_anova=df_anova.groupby(["make"])
>>> import numpy
>>> import math
>>> import scipy
>>> from scipy import stats
>>> anova_result=stats.f_oneway(group_anova.get_group("honda")["price"],group_anova.get_group("subaru")["price"])
>>> anova_result
F_onewayResult(statistic=0.19744030127462606, pvalue=0.6609478240622193)
>>> #Co-relation Statistics
>>> anova_result=stats.f_oneway(group_anova.get_group("honda")["price"],group_anova.get_group("jaguar")["price"])
>>> anova_result
F_onewayResult(statistic=400.925870564337, pvalue=1.0586193512077862e-11)
>>> #Regression plot.
>>> sns.regplot(x="engine-size",y="price",data=df)
<matplotlib.axes._subplots.AxesSubplot object at 0x000001A23CBF4940>
>>> plt.ylim(0,)
(0, 55736.30039934223)
>>> plt.show()
>>> sns.regplot(x="highway-mpg",y="price",data=df)
<matplotlib.axes._subplots.AxesSubplot object at 0x000001A23A973BA8>
>>> plt.ylim(0,)
(0, 48272.40207160877)
>>> plt.show()
>>> df=df.astype({"peak-rpm":int})
>>> sns.regplot(x="peak-rpm",y="price",data=df)
<matplotlib.axes._subplots.AxesSubplot object at 0x000001A23CD721D0>
>>> plt.ylim(0,)
(0, 47682.715562850135)
>>> plt.show()
>>> #PEARSON COEFFICENT.
>>> df=df.astype({"horse-power":int})
>>> pearson_coef, p_value=stats.pearsonr(df['horse-power'],df['price'])
>>> p_value
2.517436153884752e-30
>>> pearson_coef
0.6912939296171078
>>> #LINEAR REGRESSION.
>>> from sklearn.linear_model import LinearRegression
>>> lm=LinearRegression()
>>> X=df[['highway-mpg']]
>>> Y=df['price']
>>> lm.fit(X,Y)
LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)
>>> lm.intercept_
37800.45313154122
>>> lm.coef_
array([-807.73529374])
>>> Z=df[['horse-power', 'curved-weight', 'engine-size', 'highway-mpg']]
>>> lm.fit(Z, df['price'])
LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)
>>> lm.intercept_
-3527.43960049813
>>> lm.coef_
array([  -4.54225012,    3.10471608,  113.44806087, -175.07962843])
>>> import seaborn as sns
>>> sns.residplot(df['highway-mpg'], df['price'])
<matplotlib.axes._subplots.AxesSubplot object at 0x000001A23D311DD8>
>>> plt.show()
>>> 
