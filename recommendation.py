{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Import the libraries"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Get the data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "column_names = ['user_id', 'item_id', 'rating', 'timestamp']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "df = pd.read_csv('u.data', sep='\\t', names=column_names)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>user_id</th>\n",
       "      <th>item_id</th>\n",
       "      <th>rating</th>\n",
       "      <th>timestamp</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>50</td>\n",
       "      <td>5</td>\n",
       "      <td>881250949</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>172</td>\n",
       "      <td>5</td>\n",
       "      <td>881250949</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0</td>\n",
       "      <td>133</td>\n",
       "      <td>1</td>\n",
       "      <td>881250949</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>196</td>\n",
       "      <td>242</td>\n",
       "      <td>3</td>\n",
       "      <td>881250949</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>186</td>\n",
       "      <td>302</td>\n",
       "      <td>3</td>\n",
       "      <td>891717742</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   user_id  item_id  rating  timestamp\n",
       "0        0       50       5  881250949\n",
       "1        0      172       5  881250949\n",
       "2        0      133       1  881250949\n",
       "3      196      242       3  881250949\n",
       "4      186      302       3  891717742"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "movie_titles = pd.read_csv('Movie_Id_Titles')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>item_id</th>\n",
       "      <th>title</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Toy Story (1995)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>GoldenEye (1995)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>Four Rooms (1995)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>Get Shorty (1995)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>Copycat (1995)</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   item_id              title\n",
       "0        1   Toy Story (1995)\n",
       "1        2   GoldenEye (1995)\n",
       "2        3  Four Rooms (1995)\n",
       "3        4  Get Shorty (1995)\n",
       "4        5     Copycat (1995)"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movie_titles.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Merge them together:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "df = pd.merge(df, movie_titles, on='item_id')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>user_id</th>\n",
       "      <th>item_id</th>\n",
       "      <th>rating</th>\n",
       "      <th>timestamp</th>\n",
       "      <th>title</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>50</td>\n",
       "      <td>5</td>\n",
       "      <td>881250949</td>\n",
       "      <td>Star Wars (1977)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>290</td>\n",
       "      <td>50</td>\n",
       "      <td>5</td>\n",
       "      <td>880473582</td>\n",
       "      <td>Star Wars (1977)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>79</td>\n",
       "      <td>50</td>\n",
       "      <td>4</td>\n",
       "      <td>891271545</td>\n",
       "      <td>Star Wars (1977)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2</td>\n",
       "      <td>50</td>\n",
       "      <td>5</td>\n",
       "      <td>888552084</td>\n",
       "      <td>Star Wars (1977)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>8</td>\n",
       "      <td>50</td>\n",
       "      <td>5</td>\n",
       "      <td>879362124</td>\n",
       "      <td>Star Wars (1977)</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   user_id  item_id  rating  timestamp             title\n",
       "0        0       50       5  881250949  Star Wars (1977)\n",
       "1      290       50       5  880473582  Star Wars (1977)\n",
       "2       79       50       4  891271545  Star Wars (1977)\n",
       "3        2       50       5  888552084  Star Wars (1977)\n",
       "4        8       50       5  879362124  Star Wars (1977)"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## EDA"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Import vizualisation libraries"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "sns.set_style('white')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "title\n",
       "Marlene Dietrich: Shadow and Light (1996)            5.0\n",
       "Prefontaine (1997)                                   5.0\n",
       "Santa with Muscles (1996)                            5.0\n",
       "Star Kid (1997)                                      5.0\n",
       "Someone Else's America (1995)                        5.0\n",
       "Entertaining Angels: The Dorothy Day Story (1996)    5.0\n",
       "Saint of Fort Washington, The (1993)                 5.0\n",
       "Great Day in Harlem, A (1994)                        5.0\n",
       "They Made Me a Criminal (1939)                       5.0\n",
       "Aiqing wansui (1994)                                 5.0\n",
       "Name: rating, dtype: float64"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby('title')['rating'].mean().sort_values(ascending=False).head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "title\n",
       "Star Wars (1977)                 584\n",
       "Contact (1997)                   509\n",
       "Fargo (1996)                     508\n",
       "Return of the Jedi (1983)        507\n",
       "Liar Liar (1997)                 485\n",
       "English Patient, The (1996)      481\n",
       "Scream (1996)                    478\n",
       "Toy Story (1995)                 452\n",
       "Air Force One (1997)             431\n",
       "Independence Day (ID4) (1996)    429\n",
       "Name: rating, dtype: int64"
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby('title')['rating'].count().sort_values(ascending=False).head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### create a ratings dataframe with average rating and number of ratings:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "ratings =pd.DataFrame(df.groupby('title')['rating'].mean())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>rating</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>title</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>'Til There Was You (1997)</th>\n",
       "      <td>2.333333</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1-900 (1994)</th>\n",
       "      <td>2.600000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>101 Dalmatians (1996)</th>\n",
       "      <td>2.908257</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12 Angry Men (1957)</th>\n",
       "      <td>4.344000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>187 (1997)</th>\n",
       "      <td>3.024390</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                             rating\n",
       "title                              \n",
       "'Til There Was You (1997)  2.333333\n",
       "1-900 (1994)               2.600000\n",
       "101 Dalmatians (1996)      2.908257\n",
       "12 Angry Men (1957)        4.344000\n",
       "187 (1997)                 3.024390"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ratings.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#####  Set the number of ratings column:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "ratings['rating_numbers'] = pd.DataFrame(df.groupby('title')['rating'].count())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>rating</th>\n",
       "      <th>rating_numbers</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>title</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>'Til There Was You (1997)</th>\n",
       "      <td>2.333333</td>\n",
       "      <td>9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1-900 (1994)</th>\n",
       "      <td>2.600000</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>101 Dalmatians (1996)</th>\n",
       "      <td>2.908257</td>\n",
       "      <td>109</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12 Angry Men (1957)</th>\n",
       "      <td>4.344000</td>\n",
       "      <td>125</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>187 (1997)</th>\n",
       "      <td>3.024390</td>\n",
       "      <td>41</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                             rating  rating_numbers\n",
       "title                                              \n",
       "'Til There Was You (1997)  2.333333               9\n",
       "1-900 (1994)               2.600000               5\n",
       "101 Dalmatians (1996)      2.908257             109\n",
       "12 Angry Men (1957)        4.344000             125\n",
       "187 (1997)                 3.024390              41"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ratings.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Number of ratings histogram"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x11bae6780>"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\nvb3asGGDQqGQenp6lEwmFQwGVVFRIY/Hs+hDAAC+kTLsjzzyiDZv3ixJunTpkvLy8nTmzBmVl5dL\nkiorK9Xf3y+Xy6WSkhJ5PB55PB4VFBRoaGhIfr9/1uNHIhGNjo7e/iSSwuFwWo6zVDJ9/dMxz/Jn\n20wrYZ5oNJpyv5Rhl6SsrCw1NDTo1KlTeuONN9Tf3y/HcSRJXq9XsVhM8Xhcubm5k/t4vV7F4/GU\nx/b5fMrPz5/LMqY6PjJjU2lp6fyPs0yEw+GMXv90zLP82TbTSplnZGRm+6ab85OnbW1tOnnypJqb\nm5VMJie3JxIJ5eXlKScnR4lEYsr2G0MPALgzUob9vffe09GjRyVJd911lxzHkc/n08DAgCSpr69P\nZWVl8vv9CofDSiaTisViGh4eVnFx8eKuHgAwQ8pLMVu3btW+ffu0e/duXbt2Tfv379fatWvV3Nys\n9vZ2FRUVqaqqSm63W9XV1QoGgzLGqL6+XtnZ2XdiBgDADVKG/Vvf+pZef/31Gds7OjpmbAsEAgoE\nAulZGQBgQXiDEgBYhrADgGUIOwBYhrADgGUIOwBYhrADgGUIOwBYhrADgGUIOwBYhrADgGUIOwBY\nhrADgGUIOwBYhrADgGUIOwBYhrADgGUIOwBYhrADgGUIOwBYhrADgGUIOwBYhrADgGUIOwBYhrAD\ngGUIOwBYhrADgGUIOwBYhrADgGUIOwBYhrADgGUIOwBYJmu2G8fHx7V//3599NFHGhsbU21trR54\n4AE1NjbKcRytW7dOLS0tcrlc6u7uVldXl7KyslRbW6stW7bcqRkAADeYNey/+c1vtHr1ar366qv6\n17/+pR/84Af69re/rbq6Om3cuFEHDx5Ub2+vNmzYoFAopJ6eHiWTSQWDQVVUVMjj8dypOQAA/2/W\nsD/66KOqqqqSJBlj5Ha7NTg4qPLycklSZWWl+vv75XK5VFJSIo/HI4/Ho4KCAg0NDcnv9y/+BACA\nKWYNu9frlSTF43E999xzqqurU1tbmxzHmbw9FospHo8rNzd3yn7xeHxOC4hEIhodHV3o+qcIh8Np\nOc5SyfT1T8c8y59tM62EeaLRaMr9Zg27JH388cd69tlnFQwGtW3bNr366quTtyUSCeXl5SknJ0eJ\nRGLK9htDPxufz6f8/Pw53XeK4yMzNpWWls7/OMtEOBzO6PVPxzzLn20zrZR5RkZmtm+6WV8Vc/ny\n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\nAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x11b4be518>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "ratings['rating_numbers'].hist(bins=70)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Average rating per movie histogram"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x11c0314e0>"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\nyjClxEUAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x11bab3a20>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "ratings['rating'].hist(bins=70)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Relationship between the average rating and the actual number of ratings\n",
    "###### The larger the number of ratings, the more likely the rating of a movie is"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<seaborn.axisgrid.JointGrid at 0x11d6e25c0>"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\nJJIRz/8HCP9/dHzzMlcAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x11d6e2588>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.jointplot(x='rating', y='rating_numbers', data=ratings, alpha=0.5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Recommending Similar Movies"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's create a matrix that has the user ids on one access and the movie title on another axis. Each cell will then consist of the rating the user gave to that movie. The NaN values are due to most people not having seen most of the movies."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th>title</th>\n",
       "      <th>'Til There Was You (1997)</th>\n",
       "      <th>1-900 (1994)</th>\n",
       "      <th>101 Dalmatians (1996)</th>\n",
       "      <th>12 Angry Men (1957)</th>\n",
       "      <th>187 (1997)</th>\n",
       "      <th>2 Days in the Valley (1996)</th>\n",
       "      <th>20,000 Leagues Under the Sea (1954)</th>\n",
       "      <th>2001: A Space Odyssey (1968)</th>\n",
       "      <th>3 Ninjas: High Noon At Mega Mountain (1998)</th>\n",
       "      <th>39 Steps, The (1935)</th>\n",
       "      <th>...</th>\n",
       "      <th>Yankee Zulu (1994)</th>\n",
       "      <th>Year of the Horse (1997)</th>\n",
       "      <th>You So Crazy (1994)</th>\n",
       "      <th>Young Frankenstein (1974)</th>\n",
       "      <th>Young Guns (1988)</th>\n",
       "      <th>Young Guns II (1990)</th>\n",
       "      <th>Young Poisoner's Handbook, The (1995)</th>\n",
       "      <th>Zeus and Roxanne (1997)</th>\n",
       "      <th>unknown</th>\n",
       "      <th>Á köldum klaka (Cold Fever) (1994)</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>user_id</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>5.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4.0</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 1664 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "title    'Til There Was You (1997)  1-900 (1994)  101 Dalmatians (1996)  \\\n",
       "user_id                                                                   \n",
       "0                              NaN           NaN                    NaN   \n",
       "1                              NaN           NaN                    2.0   \n",
       "2                              NaN           NaN                    NaN   \n",
       "3                              NaN           NaN                    NaN   \n",
       "4                              NaN           NaN                    NaN   \n",
       "\n",
       "title    12 Angry Men (1957)  187 (1997)  2 Days in the Valley (1996)  \\\n",
       "user_id                                                                 \n",
       "0                        NaN         NaN                          NaN   \n",
       "1                        5.0         NaN                          NaN   \n",
       "2                        NaN         NaN                          NaN   \n",
       "3                        NaN         2.0                          NaN   \n",
       "4                        NaN         NaN                          NaN   \n",
       "\n",
       "title    20,000 Leagues Under the Sea (1954)  2001: A Space Odyssey (1968)  \\\n",
       "user_id                                                                      \n",
       "0                                        NaN                           NaN   \n",
       "1                                        3.0                           4.0   \n",
       "2                                        NaN                           NaN   \n",
       "3                                        NaN                           NaN   \n",
       "4                                        NaN                           NaN   \n",
       "\n",
       "title    3 Ninjas: High Noon At Mega Mountain (1998)  39 Steps, The (1935)  \\\n",
       "user_id                                                                      \n",
       "0                                                NaN                   NaN   \n",
       "1                                                NaN                   NaN   \n",
       "2                                                1.0                   NaN   \n",
       "3                                                NaN                   NaN   \n",
       "4                                                NaN                   NaN   \n",
       "\n",
       "title                   ...                  Yankee Zulu (1994)  \\\n",
       "user_id                 ...                                       \n",
       "0                       ...                                 NaN   \n",
       "1                       ...                                 NaN   \n",
       "2                       ...                                 NaN   \n",
       "3                       ...                                 NaN   \n",
       "4                       ...                                 NaN   \n",
       "\n",
       "title    Year of the Horse (1997)  You So Crazy (1994)  \\\n",
       "user_id                                                  \n",
       "0                             NaN                  NaN   \n",
       "1                             NaN                  NaN   \n",
       "2                             NaN                  NaN   \n",
       "3                             NaN                  NaN   \n",
       "4                             NaN                  NaN   \n",
       "\n",
       "title    Young Frankenstein (1974)  Young Guns (1988)  Young Guns II (1990)  \\\n",
       "user_id                                                                       \n",
       "0                              NaN                NaN                   NaN   \n",
       "1                              5.0                3.0                   NaN   \n",
       "2                              NaN                NaN                   NaN   \n",
       "3                              NaN                NaN                   NaN   \n",
       "4                              NaN                NaN                   NaN   \n",
       "\n",
       "title    Young Poisoner's Handbook, The (1995)  Zeus and Roxanne (1997)  \\\n",
       "user_id                                                                   \n",
       "0                                          NaN                      NaN   \n",
       "1                                          NaN                      NaN   \n",
       "2                                          NaN                      NaN   \n",
       "3                                          NaN                      NaN   \n",
       "4                                          NaN                      NaN   \n",
       "\n",
       "title    unknown  Á köldum klaka (Cold Fever) (1994)  \n",
       "user_id                                               \n",
       "0            NaN                                 NaN  \n",
       "1            4.0                                 NaN  \n",
       "2            NaN                                 NaN  \n",
       "3            NaN                                 NaN  \n",
       "4            NaN                                 NaN  \n",
       "\n",
       "[5 rows x 1664 columns]"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "moviemat = df.pivot_table(index='user_id', columns='title', values='rating')\n",
    "moviemat.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Most rated movies"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>rating</th>\n",
       "      <th>rating_numbers</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>title</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Star Wars (1977)</th>\n",
       "      <td>4.359589</td>\n",
       "      <td>584</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Contact (1997)</th>\n",
       "      <td>3.803536</td>\n",
       "      <td>509</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Fargo (1996)</th>\n",
       "      <td>4.155512</td>\n",
       "      <td>508</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Return of the Jedi (1983)</th>\n",
       "      <td>4.007890</td>\n",
       "      <td>507</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Liar Liar (1997)</th>\n",
       "      <td>3.156701</td>\n",
       "      <td>485</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>English Patient, The (1996)</th>\n",
       "      <td>3.656965</td>\n",
       "      <td>481</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Scream (1996)</th>\n",
       "      <td>3.441423</td>\n",
       "      <td>478</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Toy Story (1995)</th>\n",
       "      <td>3.878319</td>\n",
       "      <td>452</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Air Force One (1997)</th>\n",
       "      <td>3.631090</td>\n",
       "      <td>431</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Independence Day (ID4) (1996)</th>\n",
       "      <td>3.438228</td>\n",
       "      <td>429</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                 rating  rating_numbers\n",
       "title                                                  \n",
       "Star Wars (1977)               4.359589             584\n",
       "Contact (1997)                 3.803536             509\n",
       "Fargo (1996)                   4.155512             508\n",
       "Return of the Jedi (1983)      4.007890             507\n",
       "Liar Liar (1997)               3.156701             485\n",
       "English Patient, The (1996)    3.656965             481\n",
       "Scream (1996)                  3.441423             478\n",
       "Toy Story (1995)               3.878319             452\n",
       "Air Force One (1997)           3.631090             431\n",
       "Independence Day (ID4) (1996)  3.438228             429"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ratings.sort_values('rating_numbers', ascending=False).head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Let's choose two movies for our system: Starwars, a sci-fi movie. And Liar Liar, a comedy."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What are the user ratings for those two movies?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [],
   "source": [
    "starwars_user_ratings = moviemat['Star Wars (1977)']\n",
    "liar_liar_user_ratings =moviemat['Liar Liar (1997)']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "user_id\n",
       "0    5.0\n",
       "1    5.0\n",
       "2    5.0\n",
       "3    NaN\n",
       "4    5.0\n",
       "Name: Star Wars (1977), dtype: float64"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "starwars_user_ratings.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### correlation of every other movie to that specific user behaviour on the StarWars movie"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/anaconda/lib/python3.6/site-packages/numpy/lib/function_base.py:2995: RuntimeWarning: Degrees of freedom <= 0 for slice\n",
      "  c = cov(x, y, rowvar)\n",
      "/anaconda/lib/python3.6/site-packages/numpy/lib/function_base.py:2929: RuntimeWarning: divide by zero encountered in double_scalars\n",
      "  c *= 1. / np.float64(fact)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "title\n",
       "'Til There Was You (1997)    0.872872\n",
       "1-900 (1994)                -0.645497\n",
       "101 Dalmatians (1996)        0.211132\n",
       "12 Angry Men (1957)          0.184289\n",
       "187 (1997)                   0.027398\n",
       "dtype: float64"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "similar_to_starwars = moviemat.corrwith(starwars_user_ratings)\n",
    "similar_to_starwars.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### correlation of every other movie to that specific user behaviour on the Liar Liar movie"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/anaconda/lib/python3.6/site-packages/numpy/lib/function_base.py:2995: RuntimeWarning: Degrees of freedom <= 0 for slice\n",
      "  c = cov(x, y, rowvar)\n",
      "/anaconda/lib/python3.6/site-packages/numpy/lib/function_base.py:2929: RuntimeWarning: divide by zero encountered in double_scalars\n",
      "  c *= 1. / np.float64(fact)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "title\n",
       "'Til There Was You (1997)    0.118913\n",
       "1-900 (1994)                      NaN\n",
       "101 Dalmatians (1996)        0.469765\n",
       "12 Angry Men (1957)          0.066272\n",
       "187 (1997)                   0.175145\n",
       "dtype: float64"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "similar_to_liarliar = moviemat.corrwith(liar_liar_user_ratings)\n",
    "similar_to_liarliar.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### remove the NaN values and use a DF instead of Series"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "corr_starwars = pd.DataFrame(similar_to_starwars, columns=['Correlation'])\n",
    "corr_starwars.dropna(inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Correlation</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>title</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>'Til There Was You (1997)</th>\n",
       "      <td>0.872872</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1-900 (1994)</th>\n",
       "      <td>-0.645497</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>101 Dalmatians (1996)</th>\n",
       "      <td>0.211132</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12 Angry Men (1957)</th>\n",
       "      <td>0.184289</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>187 (1997)</th>\n",
       "      <td>0.027398</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                           Correlation\n",
       "title                                 \n",
       "'Til There Was You (1997)     0.872872\n",
       "1-900 (1994)                 -0.645497\n",
       "101 Dalmatians (1996)         0.211132\n",
       "12 Angry Men (1957)           0.184289\n",
       "187 (1997)                    0.027398"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "corr_starwars.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Perfectly correlated movies with StarWars? \n",
    "##### most likely these movies happen to have been seen only by one person who also happend to rate StarWars 5 stars"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Correlation</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>title</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Commandments (1997)</th>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Cosi (1996)</th>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>No Escape (1994)</th>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Stripes (1981)</th>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Man of the Year (1995)</th>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Hollow Reed (1996)</th>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Beans of Egypt, Maine, The (1994)</th>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Good Man in Africa, A (1994)</th>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Old Lady Who Walked in the Sea, The (Vieille qui marchait dans la mer, La) (1991)</th>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Outlaw, The (1943)</th>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                                    Correlation\n",
       "title                                                          \n",
       "Commandments (1997)                                         1.0\n",
       "Cosi (1996)                                                 1.0\n",
       "No Escape (1994)                                            1.0\n",
       "Stripes (1981)                                              1.0\n",
       "Man of the Year (1995)                                      1.0\n",
       "Hollow Reed (1996)                                          1.0\n",
       "Beans of Egypt, Maine, The (1994)                           1.0\n",
       "Good Man in Africa, A (1994)                                1.0\n",
       "Old Lady Who Walked in the Sea, The (Vieille qu...          1.0\n",
       "Outlaw, The (1943)                                          1.0"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "corr_starwars.sort_values('Correlation', ascending=False).head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Set a threshold for the number of ratings necessary and filter out movies that have less than a certain number of reviews"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "join the 'number of ratings' column to our dataframe"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Correlation</th>\n",
       "      <th>rating_numbers</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>title</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>'Til There Was You (1997)</th>\n",
       "      <td>0.872872</td>\n",
       "      <td>9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1-900 (1994)</th>\n",
       "      <td>-0.645497</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>101 Dalmatians (1996)</th>\n",
       "      <td>0.211132</td>\n",
       "      <td>109</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12 Angry Men (1957)</th>\n",
       "      <td>0.184289</td>\n",
       "      <td>125</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>187 (1997)</th>\n",
       "      <td>0.027398</td>\n",
       "      <td>41</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                           Correlation  rating_numbers\n",
       "title                                                 \n",
       "'Til There Was You (1997)     0.872872               9\n",
       "1-900 (1994)                 -0.645497               5\n",
       "101 Dalmatians (1996)         0.211132             109\n",
       "12 Angry Men (1957)           0.184289             125\n",
       "187 (1997)                    0.027398              41"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "corr_starwars = corr_starwars.join(ratings['rating_numbers'], how='left', lsuffix='_left', rsuffix='_right')\n",
    "corr_starwars.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "filter out movies that have less than 100 reviews (this value was chosen based off the ratings histogram from earlier)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Correlation</th>\n",
       "      <th>rating_numbers</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>title</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Star Wars (1977)</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>584</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Empire Strikes Back, The (1980)</th>\n",
       "      <td>0.748353</td>\n",
       "      <td>368</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Return of the Jedi (1983)</th>\n",
       "      <td>0.672556</td>\n",
       "      <td>507</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Raiders of the Lost Ark (1981)</th>\n",
       "      <td>0.536117</td>\n",
       "      <td>420</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Austin Powers: International Man of Mystery (1997)</th>\n",
       "      <td>0.377433</td>\n",
       "      <td>130</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                                    Correlation  \\\n",
       "title                                                             \n",
       "Star Wars (1977)                                       1.000000   \n",
       "Empire Strikes Back, The (1980)                        0.748353   \n",
       "Return of the Jedi (1983)                              0.672556   \n",
       "Raiders of the Lost Ark (1981)                         0.536117   \n",
       "Austin Powers: International Man of Mystery (1997)     0.377433   \n",
       "\n",
       "                                                    rating_numbers  \n",
       "title                                                               \n",
       "Star Wars (1977)                                               584  \n",
       "Empire Strikes Back, The (1980)                                368  \n",
       "Return of the Jedi (1983)                                      507  \n",
       "Raiders of the Lost Ark (1981)                                 420  \n",
       "Austin Powers: International Man of Mystery (1997)             130  "
      ]
     },
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "corr_starwars[corr_starwars['rating_numbers']>100].sort_values('Correlation', ascending=False).head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Perfectly correlated movies with Liar Liar?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Correlation</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>title</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>'Til There Was You (1997)</th>\n",
       "      <td>0.118913</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1-900 (1994)</th>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>101 Dalmatians (1996)</th>\n",
       "      <td>0.469765</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12 Angry Men (1957)</th>\n",
       "      <td>0.066272</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>187 (1997)</th>\n",
       "      <td>0.175145</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                           Correlation\n",
       "title                                 \n",
       "'Til There Was You (1997)     0.118913\n",
       "1-900 (1994)                       NaN\n",
       "101 Dalmatians (1996)         0.469765\n",
       "12 Angry Men (1957)           0.066272\n",
       "187 (1997)                    0.175145"
      ]
     },
     "execution_count": 87,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "corr_liarliar = pd.DataFrame(similar_to_liarliar, columns=['Correlation'])\n",
    "corr_liarliar.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### remove the NaN values and use a DF instead of Series"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "corr_liarliar.dropna(inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Correlation</th>\n",
       "      <th>rating_numbers</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>title</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>'Til There Was You (1997)</th>\n",
       "      <td>0.118913</td>\n",
       "      <td>9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>101 Dalmatians (1996)</th>\n",
       "      <td>0.469765</td>\n",
       "      <td>109</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12 Angry Men (1957)</th>\n",
       "      <td>0.066272</td>\n",
       "      <td>125</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>187 (1997)</th>\n",
       "      <td>0.175145</td>\n",
       "      <td>41</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2 Days in the Valley (1996)</th>\n",
       "      <td>0.040739</td>\n",
       "      <td>93</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                             Correlation  rating_numbers\n",
       "title                                                   \n",
       "'Til There Was You (1997)       0.118913               9\n",
       "101 Dalmatians (1996)           0.469765             109\n",
       "12 Angry Men (1957)             0.066272             125\n",
       "187 (1997)                      0.175145              41\n",
       "2 Days in the Valley (1996)     0.040739              93"
      ]
     },
     "execution_count": 89,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "corr_liarliar = corr_liarliar.join(ratings['rating_numbers'], how='left')\n",
    "corr_liarliar.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "filter out movies that have less than 100 reviews (this value was chosen randomly)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Correlation</th>\n",
       "      <th>rating_numbers</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>title</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Liar Liar (1997)</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>485</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Batman Forever (1995)</th>\n",
       "      <td>0.516968</td>\n",
       "      <td>114</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mask, The (1994)</th>\n",
       "      <td>0.484650</td>\n",
       "      <td>129</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Down Periscope (1996)</th>\n",
       "      <td>0.472681</td>\n",
       "      <td>101</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Con Air (1997)</th>\n",
       "      <td>0.469828</td>\n",
       "      <td>137</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                       Correlation  rating_numbers\n",
       "title                                             \n",
       "Liar Liar (1997)          1.000000             485\n",
       "Batman Forever (1995)     0.516968             114\n",
       "Mask, The (1994)          0.484650             129\n",
       "Down Periscope (1996)     0.472681             101\n",
       "Con Air (1997)            0.469828             137"
      ]
     },
     "execution_count": 90,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "corr_liarliar[corr_liarliar['rating_numbers']>100].sort_values('Correlation', ascending=False).head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
