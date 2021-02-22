{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import Splinter and BeautifulSoup\n",
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup as soup\n",
    "\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Set the executable path and initialize the chrome browser in splinter\n",
    "executable_path = {'executable_path': 'chromedriver'}\n",
    "browser = Browser('chrome', **executable_path)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Visit the mars nasa news site\n",
    "url = 'https://mars.nasa.gov/news/'\n",
    "browser.visit(url)\n",
    "# Optional delay for loading the page\n",
    "browser.is_element_present_by_css(\"ul.item_list li.slide\", wait_time=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "html = browser.html\n",
    "news_soup = soup(html, 'html.parser')\n",
    "slide_elem = news_soup.select_one('ul.item_list li.slide')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<div class=\"content_title\"><a href=\"/news/8867/nasas-mars-helicopter-reports-in/\" target=\"_self\">NASA's Mars Helicopter Reports In </a></div>"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "slide_elem.find(\"div\", class_='content_title')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"NASA's Mars Helicopter Reports In \""
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use the parent element to find the first `a` tag and save it as `news_title`\n",
    "news_title = slide_elem.find(\"div\", class_='content_title').get_text()\n",
    "news_title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'The technology demonstration has phoned home from where it is attached to the belly of NASA’s Perseverance rover. '"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use the parent element to find the paragraph text\n",
    "news_p = slide_elem.find('div', class_=\"article_teaser_body\").get_text()\n",
    "news_p"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Featured Images"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit URL\n",
    "url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Find and click the full image button\n",
    "full_image_elem = browser.find_by_tag('button')[1]\n",
    "full_image_elem.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Parse the resulting html with soup\n",
    "html = browser.html\n",
    "img_soup = soup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'image/featured/mars1.jpg'"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Find the relative image url\n",
    "img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')\n",
    "img_url_rel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/image/featured/mars1.jpg'"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use the base URL to create an absolute URL\n",
    "img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'\n",
    "img_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>value</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>description</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Equatorial Diameter:</th>\n",
       "      <td>6,792 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Polar Diameter:</th>\n",
       "      <td>6,752 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mass:</th>\n",
       "      <td>6.39 × 10^23 kg (0.11 Earths)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Moons:</th>\n",
       "      <td>2 (Phobos &amp; Deimos)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Orbit Distance:</th>\n",
       "      <td>227,943,824 km (1.38 AU)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Orbit Period:</th>\n",
       "      <td>687 days (1.9 years)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Surface Temperature:</th>\n",
       "      <td>-87 to -5 °C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>First Record:</th>\n",
       "      <td>2nd millennium BC</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Recorded By:</th>\n",
       "      <td>Egyptian astronomers</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                              value\n",
       "description                                        \n",
       "Equatorial Diameter:                       6,792 km\n",
       "Polar Diameter:                            6,752 km\n",
       "Mass:                 6.39 × 10^23 kg (0.11 Earths)\n",
       "Moons:                          2 (Phobos & Deimos)\n",
       "Orbit Distance:            227,943,824 km (1.38 AU)\n",
       "Orbit Period:                  687 days (1.9 years)\n",
       "Surface Temperature:                   -87 to -5 °C\n",
       "First Record:                     2nd millennium BC\n",
       "Recorded By:                   Egyptian astronomers"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_html('http://space-facts.com/mars/')[0]\n",
    "df.columns=['description', 'value']\n",
    "df.set_index('description', inplace=True)\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'<table border=\"1\" class=\"dataframe\">\\n  <thead>\\n    <tr style=\"text-align: right;\">\\n      <th></th>\\n      <th>value</th>\\n    </tr>\\n    <tr>\\n      <th>description</th>\\n      <th></th>\\n    </tr>\\n  </thead>\\n  <tbody>\\n    <tr>\\n      <th>Equatorial Diameter:</th>\\n      <td>6,792 km</td>\\n    </tr>\\n    <tr>\\n      <th>Polar Diameter:</th>\\n      <td>6,752 km</td>\\n    </tr>\\n    <tr>\\n      <th>Mass:</th>\\n      <td>6.39 × 10^23 kg (0.11 Earths)</td>\\n    </tr>\\n    <tr>\\n      <th>Moons:</th>\\n      <td>2 (Phobos &amp; Deimos)</td>\\n    </tr>\\n    <tr>\\n      <th>Orbit Distance:</th>\\n      <td>227,943,824 km (1.38 AU)</td>\\n    </tr>\\n    <tr>\\n      <th>Orbit Period:</th>\\n      <td>687 days (1.9 years)</td>\\n    </tr>\\n    <tr>\\n      <th>Surface Temperature:</th>\\n      <td>-87 to -5 °C</td>\\n    </tr>\\n    <tr>\\n      <th>First Record:</th>\\n      <td>2nd millennium BC</td>\\n    </tr>\\n    <tr>\\n      <th>Recorded By:</th>\\n      <td>Egyptian astronomers</td>\\n    </tr>\\n  </tbody>\\n</table>'"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.to_html()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Mars Weather"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit the weather website\n",
    "url = 'https://mars.nasa.gov/insight/weather/'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Parse the data\n",
    "html = browser.html\n",
    "weather_soup = soup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<table class=\"mb_table\" id=\"weather_observation\">\n",
      " <thead>\n",
      "  <tr>\n",
      "   <th colspan=\"2\" id=\"time_lbl\" scope=\"col\">\n",
      "    Time\n",
      "   </th>\n",
      "   <th colspan=\"3\" id=\"temperature_lbl\" scope=\"col\">\n",
      "    Air Temperature (\n",
      "    <span class=\"lbl_fahrenheit\">\n",
      "     °F\n",
      "    </span>\n",
      "    <span class=\"slash\">\n",
      "     |\n",
      "    </span>\n",
      "    <span class=\"lbl_celsius fadeBlack\">\n",
      "     °C\n",
      "    </span>\n",
      "    )\n",
      "   </th>\n",
      "   <th colspan=\"4\" id=\"windspeed_lbl\" scope=\"col\">\n",
      "    Wind Speed (\n",
      "    <span class=\"lbl_mph\">\n",
      "     mph\n",
      "    </span>\n",
      "    <span class=\"slash\">\n",
      "     |\n",
      "    </span>\n",
      "    <span class=\"lbl_mps fadeBlack\">\n",
      "     m/s\n",
      "    </span>\n",
      "    )\n",
      "   </th>\n",
      "   <th colspan=\"3\" id=\"pressure_lbl\" scope=\"col\">\n",
      "    Pressure (Pa)\n",
      "   </th>\n",
      "  </tr>\n",
      " </thead>\n",
      " <tbody>\n",
      "  <tr id=\"weather_top\">\n",
      "   <th class=\"sol\" scope=\"row\">\n",
      "    Date\n",
      "   </th>\n",
      "   <th class=\"sol\" scope=\"row\">\n",
      "    Sol\n",
      "   </th>\n",
      "   <td class=\"temperature max\">\n",
      "    Max.\n",
      "   </td>\n",
      "   <td class=\"temperature avg\">\n",
      "    Avg.\n",
      "   </td>\n",
      "   <td class=\"temperature min\">\n",
      "    Min.\n",
      "   </td>\n",
      "   <td class=\"windspeed max\">\n",
      "    Max.\n",
      "   </td>\n",
      "   <td class=\"windspeed avg\">\n",
      "    Avg.\n",
      "   </td>\n",
      "   <td class=\"windspeed min\">\n",
      "    Min.\n",
      "   </td>\n",
      "   <td class=\"windspeed direction\">\n",
      "    Direction\n",
      "    <br/>\n",
      "    <span style=\"font-size:x-small\">\n",
      "     (most common)\n",
      "    </span>\n",
      "   </td>\n",
      "   <td class=\"pressure max\">\n",
      "    Max.\n",
      "   </td>\n",
      "   <td class=\"pressure avg\">\n",
      "    Avg.\n",
      "   </td>\n",
      "   <td class=\"pressure min\">\n",
      "    Min.\n",
      "   </td>\n",
      "  </tr>\n",
      "  <tr>\n",
      "   <th class=\"sol\" scope=\"row\">\n",
      "    Feb. 12, 2021\n",
      "   </th>\n",
      "   <th class=\"sol\" scope=\"row\">\n",
      "    788\n",
      "   </th>\n",
      "   <td class=\"temperature max\">\n",
      "    <span class=\"fahrenheit\">\n",
      "     <nobr>\n",
      "      <span class=\"nodata\">\n",
      "       N/A\n",
      "      </span>\n",
      "     </nobr>\n",
      "    </span>\n",
      "    <span class=\"celsius\" style=\"display: none;\">\n",
      "     <nobr>\n",
      "      <span class=\"nodata\">\n",
      "       N/A\n",
      "      </span>\n",
      "     </nobr>\n",
      "    </span>\n",
      "   </td>\n",
      "   <td class=\"temperature avg\">\n",
      "    <span class=\"fahrenheit\">\n",
      "     <nobr>\n",
      "      <span class=\"nodata\">\n",
      "       N/A\n",
      "      </span>\n",
      "     </nobr>\n",
      "    </span>\n",
      "    <span class=\"celsius\" style=\"display: none;\">\n",
      "     <nobr>\n",
      "      <span class=\"nodata\">\n",
      "       N/A\n",
      "      </span>\n",
      "     </nobr>\n",
      "    </span>\n",
      "   </td>\n",
      "   <td class=\"temperature min\">\n",
      "    <span class=\"fahrenheit\">\n",
      "     <nobr>\n",
      "      <span class=\"nodata\">\n",
      "       N/A\n",
      "      </span>\n",
      "     </nobr>\n",
      "    </span>\n",
      "    <span class=\"celsius\" style=\"display: none;\">\n",
      "     <nobr>\n",
      "      <span class=\"nodata\">\n",
      "       N/A\n",
      "      </span>\n",
      "     </nobr>\n",
      "    </span>\n",
      "   </td>\n",
      "   <td class=\"windspeed max\">\n",
      "    <span class=\"mph\">\n",
      "     <span class=\"nodata\">\n",
      "      N/A\n",
      "     </span>\n",
      "    </span>\n",
      "    <span class=\"mps\" style=\"display:none\">\n",
      "     <span class=\"nodata\">\n",
      "      N/A\n",
      "     </span>\n",
      "    </span>\n",
      "   </td>\n",
      "   <td class=\"windspeed avg\">\n",
      "    <span class=\"mph\">\n",
      "     <span class=\"nodata\">\n",
      "      N/A\n",
      "     </span>\n",
      "    </span>\n",
      "    <span class=\"mps\" style=\"display:none\">\n",
      "     <span class=\"nodata\">\n",
      "      N/A\n",
      "     </span>\n",
      "    </span>\n",
      "   </td>\n",
      "   <td class=\"windspeed min\">\n",
      "    <span class=\"mph\">\n",
      "     <span class=\"nodata\">\n",
      "      N/A\n",
      "     </span>\n",
      "    </span>\n",
      "    <span class=\"mps\" style=\"display:none\">\n",
      "     <span class=\"nodata\">\n",
      "      N/A\n",
      "     </span>\n",
      "    </span>\n",
      "   </td>\n",
      "   <td class=\"windspeed point\">\n",
      "    <span class=\"nodata\">\n",
      "     N/A\n",
      "    </span>\n",
      "   </td>\n",
      "   <td class=\"pressure max\">\n",
      "    741.2\n",
      "   </td>\n",
      "   <td class=\"pressure avg\">\n",
      "    721.9\n",
      "   </td>\n",
      "   <td class=\"pressure min\">\n",
      "    700\n",
      "   </td>\n",
      "  </tr>\n",
      "  <tr>\n",
      "   <th class=\"sol\" scope=\"row\">\n",
      "    Feb. 11, 2021\n",
      "   </th>\n",
      "   <th class=\"sol\" scope=\"row\">\n",
      "    787\n",
      "   </th>\n",
      "   <td class=\"temperature max\">\n",
      "    <span class=\"fahrenheit\">\n",
      "     <nobr>\n",
      "      <span class=\"nodata\">\n",
      "       N/A\n",
      "      </span>\n",
      "     </nobr>\n",
      "    </span>\n",
      "    <span class=\"celsius\" style=\"display: none;\">\n",
      "     <nobr>\n",
      "      <span class=\"nodata\">\n",
      "       N/A\n",
      "      </span>\n",
      "     </nobr>\n",
      "    </span>\n",
      "   </td>\n",
      "   <td class=\"temperature avg\">\n",
      "    <span class=\"fahrenheit\">\n",
      "     <nobr>\n",
      "      <span class=\"nodata\">\n",
      "       N/A\n",
      "      </span>\n",
      "     </nobr>\n",
      "    </span>\n",
      "    <span class=\"celsius\" style=\"display: none;\">\n",
      "     <nobr>\n",
      "      <span class=\"nodata\">\n",
      "       N/A\n",
      "      </span>\n",
      "     </nobr>\n",
      "    </span>\n",
      "   </td>\n",
      "   <td class=\"temperature min\">\n",
      "    <span class=\"fahrenheit\">\n",
      "     <nobr>\n",
      "      <span class=\"nodata\">\n",
      "       N/A\n",
      "      </span>\n",
      "     </nobr>\n",
      "    </span>\n",
      "    <span class=\"celsius\" style=\"display: none;\">\n",
      "     <nobr>\n",
      "      <span class=\"nodata\">\n",
      "       N/A\n",
      "      </span>\n",
      "     </nobr>\n",
      "    </span>\n",
      "   </td>\n",
      "   <td class=\"windspeed max\">\n",
      "    <span class=\"mph\">\n",
      "     <span class=\"nodata\">\n",
      "      N/A\n",
      "     </span>\n",
      "    </span>\n",
      "    <span class=\"mps\" style=\"display:none\">\n",
      "     <span class=\"nodata\">\n",
      "      N/A\n",
      "     </span>\n",
      "    </span>\n",
      "   </td>\n",
      "   <td class=\"windspeed avg\">\n",
      "    <span class=\"mph\">\n",
      "     <span class=\"nodata\">\n",
      "      N/A\n",
      "     </span>\n",
      "    </span>\n",
      "    <span class=\"mps\" style=\"display:none\">\n",
      "     <span class=\"nodata\">\n",
      "      N/A\n",
      "     </span>\n",
      "    </span>\n",
      "   </td>\n",
      "   <td class=\"windspeed min\">\n",
      "    <span class=\"mph\">\n",
      "     <span class=\"nodata\">\n",
      "      N/A\n",
      "     </span>\n",
      "    </span>\n",
      "    <span class=\"mps\" style=\"display:none\">\n",
      "     <span class=\"nodata\">\n",
      "      N/A\n",
      "     </span>\n",
      "    </span>\n",
      "   </td>\n",
      "   <td class=\"windspeed point\">\n",
      "    <span class=\"nodata\">\n",
      "     N/A\n",
      "    </span>\n",
      "   </td>\n",
      "   <td class=\"pressure max\">\n",
      "    741.3\n",
      "   </td>\n",
      "   <td class=\"pressure avg\">\n",
      "    722.2\n",
      "   </td>\n",
      "   <td class=\"pressure min\">\n",
      "    699.1\n",
      "   </td>\n",
      "  </tr>\n",
      " </tbody>\n",
      "</table>\n"
     ]
    }
   ],
   "source": [
    "# Scrape the Daily Weather Report table\n",
    "weather_table = weather_soup.find('table', class_='mb_table')\n",
    "print(weather_table.prettify())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Hemispheres"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1. Use browser to visit the URL \n",
    "url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 2. Create a list to hold the images and titles.\n",
    "hemisphere_image_urls = []\n",
    "\n",
    "# 3. Write code to retrieve the image urls and titles for each hemisphere.\n",
    "links = browser.find_by_css(\"a.product-item h3\")\n",
    "\n",
    "for i in range(len(links)):\n",
    "    hemisphere = {} \n",
    "   \n",
    "    browser.find_by_css(\"a.product-item h3\")[i].click()\n",
    "    \n",
    "    sample_elem = browser.links.find_by_text('Sample').first\n",
    "    hemisphere['img_url'] = sample_elem['href']\n",
    "    \n",
    "    hemisphere['title'] = browser.find_by_css(\"h2.title\").text\n",
    "    \n",
    "    hemisphere_image_urls.append(hemisphere)\n",
    "    \n",
    "    browser.back()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg',\n",
       "  'title': 'Cerberus Hemisphere Enhanced'},\n",
       " {'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg',\n",
       "  'title': 'Schiaparelli Hemisphere Enhanced'},\n",
       " {'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg',\n",
       "  'title': 'Syrtis Major Hemisphere Enhanced'},\n",
       " {'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg',\n",
       "  'title': 'Valles Marineris Hemisphere Enhanced'}]"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 4. Print the list that holds the dictionary of each image url and title.\n",
    "hemisphere_image_urls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 5. Quit the browser\n",
    "browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "PythonData",
   "language": "python",
   "name": "pythondata"
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
   "version": "3.7.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
