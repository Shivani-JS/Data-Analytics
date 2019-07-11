#BINNING
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
