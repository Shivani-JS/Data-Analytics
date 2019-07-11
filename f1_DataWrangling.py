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
>>>#Simple Features Scaling
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
