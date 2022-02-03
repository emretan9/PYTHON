{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "12_mayıs.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyP9OwhSj4EUhk9gRRRJ6ZTn",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/emretan9/Python/blob/main/pandas.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "TgpYoP9UMsAb"
      },
      "source": [
        "import pandas as pd"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "w4vRT8uLPJYB"
      },
      "source": [
        "veriler= pd.read_table(\"https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/chipotle.tsv\")"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 399
        },
        "id": "1BazMs-rPrTk",
        "outputId": "2cb76679-d696-4198-fbd9-4587fb125612"
      },
      "source": [
        "veriler"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
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
              "      <th>order_id</th>\n",
              "      <th>quantity</th>\n",
              "      <th>item_name</th>\n",
              "      <th>choice_description</th>\n",
              "      <th>item_price</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>Chips and Fresh Tomato Salsa</td>\n",
              "      <td>NaN</td>\n",
              "      <td>$2.39</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>Izze</td>\n",
              "      <td>[Clementine]</td>\n",
              "      <td>$3.39</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>Nantucket Nectar</td>\n",
              "      <td>[Apple]</td>\n",
              "      <td>$3.39</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>Chips and Tomatillo-Green Chili Salsa</td>\n",
              "      <td>NaN</td>\n",
              "      <td>$2.39</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>Chicken Bowl</td>\n",
              "      <td>[Tomatillo-Red Chili Salsa (Hot), [Black Beans...</td>\n",
              "      <td>$16.98</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4617</th>\n",
              "      <td>1833</td>\n",
              "      <td>1</td>\n",
              "      <td>Steak Burrito</td>\n",
              "      <td>[Fresh Tomato Salsa, [Rice, Black Beans, Sour ...</td>\n",
              "      <td>$11.75</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4618</th>\n",
              "      <td>1833</td>\n",
              "      <td>1</td>\n",
              "      <td>Steak Burrito</td>\n",
              "      <td>[Fresh Tomato Salsa, [Rice, Sour Cream, Cheese...</td>\n",
              "      <td>$11.75</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4619</th>\n",
              "      <td>1834</td>\n",
              "      <td>1</td>\n",
              "      <td>Chicken Salad Bowl</td>\n",
              "      <td>[Fresh Tomato Salsa, [Fajita Vegetables, Pinto...</td>\n",
              "      <td>$11.25</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4620</th>\n",
              "      <td>1834</td>\n",
              "      <td>1</td>\n",
              "      <td>Chicken Salad Bowl</td>\n",
              "      <td>[Fresh Tomato Salsa, [Fajita Vegetables, Lettu...</td>\n",
              "      <td>$8.75</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4621</th>\n",
              "      <td>1834</td>\n",
              "      <td>1</td>\n",
              "      <td>Chicken Salad Bowl</td>\n",
              "      <td>[Fresh Tomato Salsa, [Fajita Vegetables, Pinto...</td>\n",
              "      <td>$8.75</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>4622 rows × 5 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "      order_id  ...  item_price\n",
              "0            1  ...      $2.39 \n",
              "1            1  ...      $3.39 \n",
              "2            1  ...      $3.39 \n",
              "3            1  ...      $2.39 \n",
              "4            2  ...     $16.98 \n",
              "...        ...  ...         ...\n",
              "4617      1833  ...     $11.75 \n",
              "4618      1833  ...     $11.75 \n",
              "4619      1834  ...     $11.25 \n",
              "4620      1834  ...      $8.75 \n",
              "4621      1834  ...      $8.75 \n",
              "\n",
              "[4622 rows x 5 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "nN-qKRKlQEHk"
      },
      "source": [
        "**not:** data frame excel tablolarının python daki karşılığıdır. "
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 194
        },
        "id": "b-PstWB5PzFH",
        "outputId": "e15dbf82-5463-4b70-aee7-318e61bf8e72"
      },
      "source": [
        "veriler.head()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
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
              "      <th>order_id</th>\n",
              "      <th>quantity</th>\n",
              "      <th>item_name</th>\n",
              "      <th>choice_description</th>\n",
              "      <th>item_price</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>Chips and Fresh Tomato Salsa</td>\n",
              "      <td>NaN</td>\n",
              "      <td>$2.39</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>Izze</td>\n",
              "      <td>[Clementine]</td>\n",
              "      <td>$3.39</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>Nantucket Nectar</td>\n",
              "      <td>[Apple]</td>\n",
              "      <td>$3.39</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>Chips and Tomatillo-Green Chili Salsa</td>\n",
              "      <td>NaN</td>\n",
              "      <td>$2.39</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>Chicken Bowl</td>\n",
              "      <td>[Tomatillo-Red Chili Salsa (Hot), [Black Beans...</td>\n",
              "      <td>$16.98</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   order_id  ...  item_price\n",
              "0         1  ...      $2.39 \n",
              "1         1  ...      $3.39 \n",
              "2         1  ...      $3.39 \n",
              "3         1  ...      $2.39 \n",
              "4         2  ...     $16.98 \n",
              "\n",
              "[5 rows x 5 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "42f286FxQbMx"
      },
      "source": [
        "***not:*** head ilk 5 column'u verir."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 399
        },
        "id": "zK-vnWTkQ3-Q",
        "outputId": "6ce7f1da-63d3-41ba-f88a-dd3c1d223b99"
      },
      "source": [
        "izleyiciler=pd.read_table(\"https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/u.user\")\n",
        "izleyiciler"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
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
              "      <th>1|24|M|technician|85711</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>2|53|F|other|94043</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>3|23|M|writer|32067</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>4|24|M|technician|43537</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>5|33|F|other|15213</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>6|42|M|executive|98101</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>937</th>\n",
              "      <td>939|26|F|student|33319</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>938</th>\n",
              "      <td>940|32|M|administrator|02215</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>939</th>\n",
              "      <td>941|20|M|student|97229</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>940</th>\n",
              "      <td>942|48|F|librarian|78209</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>941</th>\n",
              "      <td>943|22|M|student|77841</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>942 rows × 1 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "          1|24|M|technician|85711\n",
              "0              2|53|F|other|94043\n",
              "1             3|23|M|writer|32067\n",
              "2         4|24|M|technician|43537\n",
              "3              5|33|F|other|15213\n",
              "4          6|42|M|executive|98101\n",
              "..                            ...\n",
              "937        939|26|F|student|33319\n",
              "938  940|32|M|administrator|02215\n",
              "939        941|20|M|student|97229\n",
              "940      942|48|F|librarian|78209\n",
              "941        943|22|M|student|77841\n",
              "\n",
              "[942 rows x 1 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "7_gaJX10RTLA"
      },
      "source": [
        "sutun_basligi=[\"id\",\"yaş\",\"cinsiyet\",\"meslek\",\"posta kodu\"]"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 399
        },
        "id": "OyWt87UTRnqh",
        "outputId": "6b708c3c-983a-4916-d095-42b8f3fc786d"
      },
      "source": [
        "izleyiciler=pd.read_table(\"https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/u.user\",names=sutun_basligi, sep=\"|\")\n",
        "izleyiciler"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
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
              "      <th>id</th>\n",
              "      <th>yaş</th>\n",
              "      <th>cinsiyet</th>\n",
              "      <th>meslek</th>\n",
              "      <th>posta kodu</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>24</td>\n",
              "      <td>M</td>\n",
              "      <td>technician</td>\n",
              "      <td>85711</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>53</td>\n",
              "      <td>F</td>\n",
              "      <td>other</td>\n",
              "      <td>94043</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>23</td>\n",
              "      <td>M</td>\n",
              "      <td>writer</td>\n",
              "      <td>32067</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4</td>\n",
              "      <td>24</td>\n",
              "      <td>M</td>\n",
              "      <td>technician</td>\n",
              "      <td>43537</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5</td>\n",
              "      <td>33</td>\n",
              "      <td>F</td>\n",
              "      <td>other</td>\n",
              "      <td>15213</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>938</th>\n",
              "      <td>939</td>\n",
              "      <td>26</td>\n",
              "      <td>F</td>\n",
              "      <td>student</td>\n",
              "      <td>33319</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>939</th>\n",
              "      <td>940</td>\n",
              "      <td>32</td>\n",
              "      <td>M</td>\n",
              "      <td>administrator</td>\n",
              "      <td>02215</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>940</th>\n",
              "      <td>941</td>\n",
              "      <td>20</td>\n",
              "      <td>M</td>\n",
              "      <td>student</td>\n",
              "      <td>97229</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>941</th>\n",
              "      <td>942</td>\n",
              "      <td>48</td>\n",
              "      <td>F</td>\n",
              "      <td>librarian</td>\n",
              "      <td>78209</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>942</th>\n",
              "      <td>943</td>\n",
              "      <td>22</td>\n",
              "      <td>M</td>\n",
              "      <td>student</td>\n",
              "      <td>77841</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>943 rows × 5 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "      id  yaş cinsiyet         meslek posta kodu\n",
              "0      1   24        M     technician      85711\n",
              "1      2   53        F          other      94043\n",
              "2      3   23        M         writer      32067\n",
              "3      4   24        M     technician      43537\n",
              "4      5   33        F          other      15213\n",
              "..   ...  ...      ...            ...        ...\n",
              "938  939   26        F        student      33319\n",
              "939  940   32        M  administrator      02215\n",
              "940  941   20        M        student      97229\n",
              "941  942   48        F      librarian      78209\n",
              "942  943   22        M        student      77841\n",
              "\n",
              "[943 rows x 5 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 399
        },
        "id": "UUS5jmY7S17V",
        "outputId": "6ffc0b94-5ee1-43c7-951a-352c4c04e896"
      },
      "source": [
        "ufo=pd.read_csv(\"https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv\")\n",
        "ufo"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
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
              "      <th>City</th>\n",
              "      <th>Colors Reported</th>\n",
              "      <th>Shape Reported</th>\n",
              "      <th>State</th>\n",
              "      <th>Time</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Ithaca</td>\n",
              "      <td>NaN</td>\n",
              "      <td>TRIANGLE</td>\n",
              "      <td>NY</td>\n",
              "      <td>6/1/1930 22:00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Willingboro</td>\n",
              "      <td>NaN</td>\n",
              "      <td>OTHER</td>\n",
              "      <td>NJ</td>\n",
              "      <td>6/30/1930 20:00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Holyoke</td>\n",
              "      <td>NaN</td>\n",
              "      <td>OVAL</td>\n",
              "      <td>CO</td>\n",
              "      <td>2/15/1931 14:00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Abilene</td>\n",
              "      <td>NaN</td>\n",
              "      <td>DISK</td>\n",
              "      <td>KS</td>\n",
              "      <td>6/1/1931 13:00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>New York Worlds Fair</td>\n",
              "      <td>NaN</td>\n",
              "      <td>LIGHT</td>\n",
              "      <td>NY</td>\n",
              "      <td>4/18/1933 19:00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>18236</th>\n",
              "      <td>Grant Park</td>\n",
              "      <td>NaN</td>\n",
              "      <td>TRIANGLE</td>\n",
              "      <td>IL</td>\n",
              "      <td>12/31/2000 23:00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>18237</th>\n",
              "      <td>Spirit Lake</td>\n",
              "      <td>NaN</td>\n",
              "      <td>DISK</td>\n",
              "      <td>IA</td>\n",
              "      <td>12/31/2000 23:00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>18238</th>\n",
              "      <td>Eagle River</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>WI</td>\n",
              "      <td>12/31/2000 23:45</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>18239</th>\n",
              "      <td>Eagle River</td>\n",
              "      <td>RED</td>\n",
              "      <td>LIGHT</td>\n",
              "      <td>WI</td>\n",
              "      <td>12/31/2000 23:45</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>18240</th>\n",
              "      <td>Ybor</td>\n",
              "      <td>NaN</td>\n",
              "      <td>OVAL</td>\n",
              "      <td>FL</td>\n",
              "      <td>12/31/2000 23:59</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>18241 rows × 5 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "                       City Colors Reported  ... State              Time\n",
              "0                    Ithaca             NaN  ...    NY    6/1/1930 22:00\n",
              "1               Willingboro             NaN  ...    NJ   6/30/1930 20:00\n",
              "2                   Holyoke             NaN  ...    CO   2/15/1931 14:00\n",
              "3                   Abilene             NaN  ...    KS    6/1/1931 13:00\n",
              "4      New York Worlds Fair             NaN  ...    NY   4/18/1933 19:00\n",
              "...                     ...             ...  ...   ...               ...\n",
              "18236            Grant Park             NaN  ...    IL  12/31/2000 23:00\n",
              "18237           Spirit Lake             NaN  ...    IA  12/31/2000 23:00\n",
              "18238           Eagle River             NaN  ...    WI  12/31/2000 23:45\n",
              "18239           Eagle River             RED  ...    WI  12/31/2000 23:45\n",
              "18240                  Ybor             NaN  ...    FL  12/31/2000 23:59\n",
              "\n",
              "[18241 rows x 5 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 36
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hDuX6GnhTYNP",
        "outputId": "8c36f743-9f70-42c1-ffd9-9bed74d102b1"
      },
      "source": [
        "ufo[\"City\"]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0                      Ithaca\n",
              "1                 Willingboro\n",
              "2                     Holyoke\n",
              "3                     Abilene\n",
              "4        New York Worlds Fair\n",
              "                 ...         \n",
              "18236              Grant Park\n",
              "18237             Spirit Lake\n",
              "18238             Eagle River\n",
              "18239             Eagle River\n",
              "18240                    Ybor\n",
              "Name: City, Length: 18241, dtype: object"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 16
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ggPEw93xTzYC",
        "outputId": "99723394-efbb-4315-90e0-c09cbc3c14ed"
      },
      "source": [
        "ufo.State"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0        NY\n",
              "1        NJ\n",
              "2        CO\n",
              "3        KS\n",
              "4        NY\n",
              "         ..\n",
              "18236    IL\n",
              "18237    IA\n",
              "18238    WI\n",
              "18239    WI\n",
              "18240    FL\n",
              "Name: State, Length: 18241, dtype: object"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 19
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "b2J6KQN3Te2N",
        "outputId": "10fac963-86b0-4e2f-fcc4-fcefb4ec14dc"
      },
      "source": [
        "ufo[\"Colors Reported\"]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0        NaN\n",
              "1        NaN\n",
              "2        NaN\n",
              "3        NaN\n",
              "4        NaN\n",
              "        ... \n",
              "18236    NaN\n",
              "18237    NaN\n",
              "18238    NaN\n",
              "18239    RED\n",
              "18240    NaN\n",
              "Name: Colors Reported, Length: 18241, dtype: object"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 18
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "m8TnkGmMT6TH",
        "outputId": "54317ddf-67de-43c6-92ab-38646bdda11d"
      },
      "source": [
        "ufo.shape"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(18241, 5)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 20
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 164
        },
        "id": "ZXnDGH51UCsf",
        "outputId": "d06c8e77-f3a6-43bf-f2ba-a56e7b539e88"
      },
      "source": [
        "ufo.describe()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
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
              "      <th>City</th>\n",
              "      <th>Colors Reported</th>\n",
              "      <th>Shape Reported</th>\n",
              "      <th>State</th>\n",
              "      <th>Time</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>18216</td>\n",
              "      <td>2882</td>\n",
              "      <td>15597</td>\n",
              "      <td>18241</td>\n",
              "      <td>18241</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>unique</th>\n",
              "      <td>6476</td>\n",
              "      <td>27</td>\n",
              "      <td>27</td>\n",
              "      <td>52</td>\n",
              "      <td>16145</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>top</th>\n",
              "      <td>Seattle</td>\n",
              "      <td>RED</td>\n",
              "      <td>LIGHT</td>\n",
              "      <td>CA</td>\n",
              "      <td>11/16/1999 19:00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>freq</th>\n",
              "      <td>187</td>\n",
              "      <td>780</td>\n",
              "      <td>2803</td>\n",
              "      <td>2529</td>\n",
              "      <td>27</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "           City Colors Reported Shape Reported  State              Time\n",
              "count     18216            2882          15597  18241             18241\n",
              "unique     6476              27             27     52             16145\n",
              "top     Seattle             RED          LIGHT     CA  11/16/1999 19:00\n",
              "freq        187             780           2803   2529                27"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 25
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wiXesYasUd5a",
        "outputId": "7453dc10-a907-4da8-c917-78e105bef24a"
      },
      "source": [
        "type(ufo)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "pandas.core.frame.DataFrame"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 22
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ao7b0xEiYfFB",
        "outputId": "0bfa692a-67e8-4484-be69-edf3f523ccde"
      },
      "source": [
        "ufo.columns"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Index(['City', 'Colors Reported', 'Shape Reported', 'State', 'Time'], dtype='object')"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 32
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BFaZBrAQYfpz",
        "outputId": "3297b3b6-ae7e-4b81-a0cf-66a1a822ed8f"
      },
      "source": [
        "ufo.columns=ufo.columns.str.replace(\" \" , \"_\")\n",
        "ufo.columns"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Index(['City', 'Colors_Reported', 'Shape_Reported', 'State', 'Time'], dtype='object')"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 38
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DwyK0HRrZiH4",
        "outputId": "9c7ee42f-193b-414f-83e3-ed5d10986815"
      },
      "source": [
        "ufo.Colors_Reported"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0        NaN\n",
              "1        NaN\n",
              "2        NaN\n",
              "3        NaN\n",
              "4        NaN\n",
              "        ... \n",
              "18236    NaN\n",
              "18237    NaN\n",
              "18238    NaN\n",
              "18239    RED\n",
              "18240    NaN\n",
              "Name: Colors_Reported, Length: 18241, dtype: object"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 39
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 399
        },
        "id": "ZFD0Va75aAZ8",
        "outputId": "37cded0e-704d-4608-e56b-ba2b1f19360b"
      },
      "source": [
        "movies=pd.read_csv(\"https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/imdb_1000.csv\")\n",
        "movies"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
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
              "      <th>star_rating</th>\n",
              "      <th>title</th>\n",
              "      <th>content_rating</th>\n",
              "      <th>genre</th>\n",
              "      <th>duration</th>\n",
              "      <th>actors_list</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>9.3</td>\n",
              "      <td>The Shawshank Redemption</td>\n",
              "      <td>R</td>\n",
              "      <td>Crime</td>\n",
              "      <td>142</td>\n",
              "      <td>[u'Tim Robbins', u'Morgan Freeman', u'Bob Gunt...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>9.2</td>\n",
              "      <td>The Godfather</td>\n",
              "      <td>R</td>\n",
              "      <td>Crime</td>\n",
              "      <td>175</td>\n",
              "      <td>[u'Marlon Brando', u'Al Pacino', u'James Caan']</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>9.1</td>\n",
              "      <td>The Godfather: Part II</td>\n",
              "      <td>R</td>\n",
              "      <td>Crime</td>\n",
              "      <td>200</td>\n",
              "      <td>[u'Al Pacino', u'Robert De Niro', u'Robert Duv...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>9.0</td>\n",
              "      <td>The Dark Knight</td>\n",
              "      <td>PG-13</td>\n",
              "      <td>Action</td>\n",
              "      <td>152</td>\n",
              "      <td>[u'Christian Bale', u'Heath Ledger', u'Aaron E...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>8.9</td>\n",
              "      <td>Pulp Fiction</td>\n",
              "      <td>R</td>\n",
              "      <td>Crime</td>\n",
              "      <td>154</td>\n",
              "      <td>[u'John Travolta', u'Uma Thurman', u'Samuel L....</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>974</th>\n",
              "      <td>7.4</td>\n",
              "      <td>Tootsie</td>\n",
              "      <td>PG</td>\n",
              "      <td>Comedy</td>\n",
              "      <td>116</td>\n",
              "      <td>[u'Dustin Hoffman', u'Jessica Lange', u'Teri G...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>975</th>\n",
              "      <td>7.4</td>\n",
              "      <td>Back to the Future Part III</td>\n",
              "      <td>PG</td>\n",
              "      <td>Adventure</td>\n",
              "      <td>118</td>\n",
              "      <td>[u'Michael J. Fox', u'Christopher Lloyd', u'Ma...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>976</th>\n",
              "      <td>7.4</td>\n",
              "      <td>Master and Commander: The Far Side of the World</td>\n",
              "      <td>PG-13</td>\n",
              "      <td>Action</td>\n",
              "      <td>138</td>\n",
              "      <td>[u'Russell Crowe', u'Paul Bettany', u'Billy Bo...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>977</th>\n",
              "      <td>7.4</td>\n",
              "      <td>Poltergeist</td>\n",
              "      <td>PG</td>\n",
              "      <td>Horror</td>\n",
              "      <td>114</td>\n",
              "      <td>[u'JoBeth Williams', u\"Heather O'Rourke\", u'Cr...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>978</th>\n",
              "      <td>7.4</td>\n",
              "      <td>Wall Street</td>\n",
              "      <td>R</td>\n",
              "      <td>Crime</td>\n",
              "      <td>126</td>\n",
              "      <td>[u'Charlie Sheen', u'Michael Douglas', u'Tamar...</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>979 rows × 6 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "     star_rating  ...                                        actors_list\n",
              "0            9.3  ...  [u'Tim Robbins', u'Morgan Freeman', u'Bob Gunt...\n",
              "1            9.2  ...    [u'Marlon Brando', u'Al Pacino', u'James Caan']\n",
              "2            9.1  ...  [u'Al Pacino', u'Robert De Niro', u'Robert Duv...\n",
              "3            9.0  ...  [u'Christian Bale', u'Heath Ledger', u'Aaron E...\n",
              "4            8.9  ...  [u'John Travolta', u'Uma Thurman', u'Samuel L....\n",
              "..           ...  ...                                                ...\n",
              "974          7.4  ...  [u'Dustin Hoffman', u'Jessica Lange', u'Teri G...\n",
              "975          7.4  ...  [u'Michael J. Fox', u'Christopher Lloyd', u'Ma...\n",
              "976          7.4  ...  [u'Russell Crowe', u'Paul Bettany', u'Billy Bo...\n",
              "977          7.4  ...  [u'JoBeth Williams', u\"Heather O'Rourke\", u'Cr...\n",
              "978          7.4  ...  [u'Charlie Sheen', u'Michael Douglas', u'Tamar...\n",
              "\n",
              "[979 rows x 6 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 41
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zRGTvGmWaQZg",
        "outputId": "950b0f2f-b516-48d8-b779-c53b7ab785a2"
      },
      "source": [
        "movies[\"title\"].sort_values()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "542     (500) Days of Summer\n",
              "5               12 Angry Men\n",
              "201         12 Years a Slave\n",
              "698                127 Hours\n",
              "110    2001: A Space Odyssey\n",
              "               ...          \n",
              "955         Zero Dark Thirty\n",
              "677                   Zodiac\n",
              "615               Zombieland\n",
              "526                     Zulu\n",
              "864                    [Rec]\n",
              "Name: title, Length: 979, dtype: object"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 42
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QImxW8_UavEg",
        "outputId": "b74ea7de-f379-4f72-8684-0b2646b9f23c"
      },
      "source": [
        "movies[\"title\"].sort_values(ascending=False)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "864                    [Rec]\n",
              "526                     Zulu\n",
              "615               Zombieland\n",
              "677                   Zodiac\n",
              "955         Zero Dark Thirty\n",
              "               ...          \n",
              "110    2001: A Space Odyssey\n",
              "698                127 Hours\n",
              "201         12 Years a Slave\n",
              "5               12 Angry Men\n",
              "542     (500) Days of Summer\n",
              "Name: title, Length: 979, dtype: object"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 43
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 399
        },
        "id": "uQULxL3ka9b5",
        "outputId": "06c4cf10-2334-483b-b072-4b204ef0cf0f"
      },
      "source": [
        "movies.sort_values(\"title\",ascending=False)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
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
              "      <th>star_rating</th>\n",
              "      <th>title</th>\n",
              "      <th>content_rating</th>\n",
              "      <th>genre</th>\n",
              "      <th>duration</th>\n",
              "      <th>actors_list</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>864</th>\n",
              "      <td>7.5</td>\n",
              "      <td>[Rec]</td>\n",
              "      <td>R</td>\n",
              "      <td>Horror</td>\n",
              "      <td>78</td>\n",
              "      <td>[u'Manuela Velasco', u'Ferran Terraza', u'Jorg...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>526</th>\n",
              "      <td>7.8</td>\n",
              "      <td>Zulu</td>\n",
              "      <td>UNRATED</td>\n",
              "      <td>Drama</td>\n",
              "      <td>138</td>\n",
              "      <td>[u'Stanley Baker', u'Jack Hawkins', u'Ulla Jac...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>615</th>\n",
              "      <td>7.7</td>\n",
              "      <td>Zombieland</td>\n",
              "      <td>R</td>\n",
              "      <td>Comedy</td>\n",
              "      <td>88</td>\n",
              "      <td>[u'Jesse Eisenberg', u'Emma Stone', u'Woody Ha...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>677</th>\n",
              "      <td>7.7</td>\n",
              "      <td>Zodiac</td>\n",
              "      <td>R</td>\n",
              "      <td>Crime</td>\n",
              "      <td>157</td>\n",
              "      <td>[u'Jake Gyllenhaal', u'Robert Downey Jr.', u'M...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>955</th>\n",
              "      <td>7.4</td>\n",
              "      <td>Zero Dark Thirty</td>\n",
              "      <td>R</td>\n",
              "      <td>Drama</td>\n",
              "      <td>157</td>\n",
              "      <td>[u'Jessica Chastain', u'Joel Edgerton', u'Chri...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>110</th>\n",
              "      <td>8.3</td>\n",
              "      <td>2001: A Space Odyssey</td>\n",
              "      <td>G</td>\n",
              "      <td>Mystery</td>\n",
              "      <td>160</td>\n",
              "      <td>[u'Keir Dullea', u'Gary Lockwood', u'William S...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>698</th>\n",
              "      <td>7.6</td>\n",
              "      <td>127 Hours</td>\n",
              "      <td>R</td>\n",
              "      <td>Adventure</td>\n",
              "      <td>94</td>\n",
              "      <td>[u'James Franco', u'Amber Tamblyn', u'Kate Mara']</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>201</th>\n",
              "      <td>8.1</td>\n",
              "      <td>12 Years a Slave</td>\n",
              "      <td>R</td>\n",
              "      <td>Biography</td>\n",
              "      <td>134</td>\n",
              "      <td>[u'Chiwetel Ejiofor', u'Michael Kenneth Willia...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>8.9</td>\n",
              "      <td>12 Angry Men</td>\n",
              "      <td>NOT RATED</td>\n",
              "      <td>Drama</td>\n",
              "      <td>96</td>\n",
              "      <td>[u'Henry Fonda', u'Lee J. Cobb', u'Martin Bals...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>542</th>\n",
              "      <td>7.8</td>\n",
              "      <td>(500) Days of Summer</td>\n",
              "      <td>PG-13</td>\n",
              "      <td>Comedy</td>\n",
              "      <td>95</td>\n",
              "      <td>[u'Zooey Deschanel', u'Joseph Gordon-Levitt', ...</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>979 rows × 6 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "     star_rating  ...                                        actors_list\n",
              "864          7.5  ...  [u'Manuela Velasco', u'Ferran Terraza', u'Jorg...\n",
              "526          7.8  ...  [u'Stanley Baker', u'Jack Hawkins', u'Ulla Jac...\n",
              "615          7.7  ...  [u'Jesse Eisenberg', u'Emma Stone', u'Woody Ha...\n",
              "677          7.7  ...  [u'Jake Gyllenhaal', u'Robert Downey Jr.', u'M...\n",
              "955          7.4  ...  [u'Jessica Chastain', u'Joel Edgerton', u'Chri...\n",
              "..           ...  ...                                                ...\n",
              "110          8.3  ...  [u'Keir Dullea', u'Gary Lockwood', u'William S...\n",
              "698          7.6  ...  [u'James Franco', u'Amber Tamblyn', u'Kate Mara']\n",
              "201          8.1  ...  [u'Chiwetel Ejiofor', u'Michael Kenneth Willia...\n",
              "5            8.9  ...  [u'Henry Fonda', u'Lee J. Cobb', u'Martin Bals...\n",
              "542          7.8  ...  [u'Zooey Deschanel', u'Joseph Gordon-Levitt', ...\n",
              "\n",
              "[979 rows x 6 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 45
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 194
        },
        "id": "1AgUFfYzbasg",
        "outputId": "fc5358b5-6720-4624-877b-431f6b4c68d3"
      },
      "source": [
        "movies.head()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
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
              "      <th>star_rating</th>\n",
              "      <th>title</th>\n",
              "      <th>content_rating</th>\n",
              "      <th>genre</th>\n",
              "      <th>duration</th>\n",
              "      <th>actors_list</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>9.3</td>\n",
              "      <td>The Shawshank Redemption</td>\n",
              "      <td>R</td>\n",
              "      <td>Crime</td>\n",
              "      <td>142</td>\n",
              "      <td>[u'Tim Robbins', u'Morgan Freeman', u'Bob Gunt...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>9.2</td>\n",
              "      <td>The Godfather</td>\n",
              "      <td>R</td>\n",
              "      <td>Crime</td>\n",
              "      <td>175</td>\n",
              "      <td>[u'Marlon Brando', u'Al Pacino', u'James Caan']</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>9.1</td>\n",
              "      <td>The Godfather: Part II</td>\n",
              "      <td>R</td>\n",
              "      <td>Crime</td>\n",
              "      <td>200</td>\n",
              "      <td>[u'Al Pacino', u'Robert De Niro', u'Robert Duv...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>9.0</td>\n",
              "      <td>The Dark Knight</td>\n",
              "      <td>PG-13</td>\n",
              "      <td>Action</td>\n",
              "      <td>152</td>\n",
              "      <td>[u'Christian Bale', u'Heath Ledger', u'Aaron E...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>8.9</td>\n",
              "      <td>Pulp Fiction</td>\n",
              "      <td>R</td>\n",
              "      <td>Crime</td>\n",
              "      <td>154</td>\n",
              "      <td>[u'John Travolta', u'Uma Thurman', u'Samuel L....</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   star_rating  ...                                        actors_list\n",
              "0          9.3  ...  [u'Tim Robbins', u'Morgan Freeman', u'Bob Gunt...\n",
              "1          9.2  ...    [u'Marlon Brando', u'Al Pacino', u'James Caan']\n",
              "2          9.1  ...  [u'Al Pacino', u'Robert De Niro', u'Robert Duv...\n",
              "3          9.0  ...  [u'Christian Bale', u'Heath Ledger', u'Aaron E...\n",
              "4          8.9  ...  [u'John Travolta', u'Uma Thurman', u'Samuel L....\n",
              "\n",
              "[5 rows x 6 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 47
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 76
        },
        "id": "BlkuHvL9bKsY",
        "outputId": "e599f453-7731-4c4e-c028-57af262b4dbc"
      },
      "source": [
        "movies[2:3]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
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
              "      <th>star_rating</th>\n",
              "      <th>title</th>\n",
              "      <th>content_rating</th>\n",
              "      <th>genre</th>\n",
              "      <th>duration</th>\n",
              "      <th>actors_list</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>9.1</td>\n",
              "      <td>The Godfather: Part II</td>\n",
              "      <td>R</td>\n",
              "      <td>Crime</td>\n",
              "      <td>200</td>\n",
              "      <td>[u'Al Pacino', u'Robert De Niro', u'Robert Duv...</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   star_rating  ...                                        actors_list\n",
              "2          9.1  ...  [u'Al Pacino', u'Robert De Niro', u'Robert Duv...\n",
              "\n",
              "[1 rows x 6 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 46
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "llJ2rqb5bSD5"
      },
      "source": [
        "***not:***2 ve 3 arasını aldı."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 135
        },
        "id": "oqHwo1nIbXKj",
        "outputId": "e0724143-c34a-4edc-d44f-9fae8fc8c937"
      },
      "source": [
        "movies.iloc[1:4, 1:3]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
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
              "      <th>title</th>\n",
              "      <th>content_rating</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>The Godfather</td>\n",
              "      <td>R</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>The Godfather: Part II</td>\n",
              "      <td>R</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>The Dark Knight</td>\n",
              "      <td>PG-13</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "                    title content_rating\n",
              "1           The Godfather              R\n",
              "2  The Godfather: Part II              R\n",
              "3         The Dark Knight          PG-13"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 48
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "qAl-zrSAbpWA"
      },
      "source": [
        "***not:***1 le 4 arası satır al 1 le 3 arası sütun al demek "
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 399
        },
        "id": "3hB6lLFzbzx4",
        "outputId": "404ba12f-d66d-4c2b-ff9f-88b0a231a36b"
      },
      "source": [
        "movies[movies.duration >= 200]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
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
              "      <th>star_rating</th>\n",
              "      <th>title</th>\n",
              "      <th>content_rating</th>\n",
              "      <th>genre</th>\n",
              "      <th>duration</th>\n",
              "      <th>actors_list</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>9.1</td>\n",
              "      <td>The Godfather: Part II</td>\n",
              "      <td>R</td>\n",
              "      <td>Crime</td>\n",
              "      <td>200</td>\n",
              "      <td>[u'Al Pacino', u'Robert De Niro', u'Robert Duv...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>8.9</td>\n",
              "      <td>The Lord of the Rings: The Return of the King</td>\n",
              "      <td>PG-13</td>\n",
              "      <td>Adventure</td>\n",
              "      <td>201</td>\n",
              "      <td>[u'Elijah Wood', u'Viggo Mortensen', u'Ian McK...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>17</th>\n",
              "      <td>8.7</td>\n",
              "      <td>Seven Samurai</td>\n",
              "      <td>UNRATED</td>\n",
              "      <td>Drama</td>\n",
              "      <td>207</td>\n",
              "      <td>[u'Toshir\\xf4 Mifune', u'Takashi Shimura', u'K...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>78</th>\n",
              "      <td>8.4</td>\n",
              "      <td>Once Upon a Time in America</td>\n",
              "      <td>R</td>\n",
              "      <td>Crime</td>\n",
              "      <td>229</td>\n",
              "      <td>[u'Robert De Niro', u'James Woods', u'Elizabet...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>85</th>\n",
              "      <td>8.4</td>\n",
              "      <td>Lawrence of Arabia</td>\n",
              "      <td>PG</td>\n",
              "      <td>Adventure</td>\n",
              "      <td>216</td>\n",
              "      <td>[u\"Peter O'Toole\", u'Alec Guinness', u'Anthony...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>142</th>\n",
              "      <td>8.3</td>\n",
              "      <td>Lagaan: Once Upon a Time in India</td>\n",
              "      <td>PG</td>\n",
              "      <td>Adventure</td>\n",
              "      <td>224</td>\n",
              "      <td>[u'Aamir Khan', u'Gracy Singh', u'Rachel Shell...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>157</th>\n",
              "      <td>8.2</td>\n",
              "      <td>Gone with the Wind</td>\n",
              "      <td>G</td>\n",
              "      <td>Drama</td>\n",
              "      <td>238</td>\n",
              "      <td>[u'Clark Gable', u'Vivien Leigh', u'Thomas Mit...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>204</th>\n",
              "      <td>8.1</td>\n",
              "      <td>Ben-Hur</td>\n",
              "      <td>G</td>\n",
              "      <td>Adventure</td>\n",
              "      <td>212</td>\n",
              "      <td>[u'Charlton Heston', u'Jack Hawkins', u'Stephe...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>445</th>\n",
              "      <td>7.9</td>\n",
              "      <td>The Ten Commandments</td>\n",
              "      <td>APPROVED</td>\n",
              "      <td>Adventure</td>\n",
              "      <td>220</td>\n",
              "      <td>[u'Charlton Heston', u'Yul Brynner', u'Anne Ba...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>476</th>\n",
              "      <td>7.8</td>\n",
              "      <td>Hamlet</td>\n",
              "      <td>PG-13</td>\n",
              "      <td>Drama</td>\n",
              "      <td>242</td>\n",
              "      <td>[u'Kenneth Branagh', u'Julie Christie', u'Dere...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>630</th>\n",
              "      <td>7.7</td>\n",
              "      <td>Malcolm X</td>\n",
              "      <td>PG-13</td>\n",
              "      <td>Biography</td>\n",
              "      <td>202</td>\n",
              "      <td>[u'Denzel Washington', u'Angela Bassett', u'De...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>767</th>\n",
              "      <td>7.6</td>\n",
              "      <td>It's a Mad, Mad, Mad, Mad World</td>\n",
              "      <td>APPROVED</td>\n",
              "      <td>Action</td>\n",
              "      <td>205</td>\n",
              "      <td>[u'Spencer Tracy', u'Milton Berle', u'Ethel Me...</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "     star_rating  ...                                        actors_list\n",
              "2            9.1  ...  [u'Al Pacino', u'Robert De Niro', u'Robert Duv...\n",
              "7            8.9  ...  [u'Elijah Wood', u'Viggo Mortensen', u'Ian McK...\n",
              "17           8.7  ...  [u'Toshir\\xf4 Mifune', u'Takashi Shimura', u'K...\n",
              "78           8.4  ...  [u'Robert De Niro', u'James Woods', u'Elizabet...\n",
              "85           8.4  ...  [u\"Peter O'Toole\", u'Alec Guinness', u'Anthony...\n",
              "142          8.3  ...  [u'Aamir Khan', u'Gracy Singh', u'Rachel Shell...\n",
              "157          8.2  ...  [u'Clark Gable', u'Vivien Leigh', u'Thomas Mit...\n",
              "204          8.1  ...  [u'Charlton Heston', u'Jack Hawkins', u'Stephe...\n",
              "445          7.9  ...  [u'Charlton Heston', u'Yul Brynner', u'Anne Ba...\n",
              "476          7.8  ...  [u'Kenneth Branagh', u'Julie Christie', u'Dere...\n",
              "630          7.7  ...  [u'Denzel Washington', u'Angela Bassett', u'De...\n",
              "767          7.6  ...  [u'Spencer Tracy', u'Milton Berle', u'Ethel Me...\n",
              "\n",
              "[12 rows x 6 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 49
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 135
        },
        "id": "np0ZFkvNdUhm",
        "outputId": "2742a66b-c6f8-4fc7-c991-67ba4ad951ea"
      },
      "source": [
        "movies[(movies.duration >= 200) & (movies.genre ==\"Drama\")]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
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
              "      <th>star_rating</th>\n",
              "      <th>title</th>\n",
              "      <th>content_rating</th>\n",
              "      <th>genre</th>\n",
              "      <th>duration</th>\n",
              "      <th>actors_list</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>17</th>\n",
              "      <td>8.7</td>\n",
              "      <td>Seven Samurai</td>\n",
              "      <td>UNRATED</td>\n",
              "      <td>Drama</td>\n",
              "      <td>207</td>\n",
              "      <td>[u'Toshir\\xf4 Mifune', u'Takashi Shimura', u'K...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>157</th>\n",
              "      <td>8.2</td>\n",
              "      <td>Gone with the Wind</td>\n",
              "      <td>G</td>\n",
              "      <td>Drama</td>\n",
              "      <td>238</td>\n",
              "      <td>[u'Clark Gable', u'Vivien Leigh', u'Thomas Mit...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>476</th>\n",
              "      <td>7.8</td>\n",
              "      <td>Hamlet</td>\n",
              "      <td>PG-13</td>\n",
              "      <td>Drama</td>\n",
              "      <td>242</td>\n",
              "      <td>[u'Kenneth Branagh', u'Julie Christie', u'Dere...</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "     star_rating  ...                                        actors_list\n",
              "17           8.7  ...  [u'Toshir\\xf4 Mifune', u'Takashi Shimura', u'K...\n",
              "157          8.2  ...  [u'Clark Gable', u'Vivien Leigh', u'Thomas Mit...\n",
              "476          7.8  ...  [u'Kenneth Branagh', u'Julie Christie', u'Dere...\n",
              "\n",
              "[3 rows x 6 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 50
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 568
        },
        "id": "xBntXgDkdthP",
        "outputId": "6b062deb-8dc1-4325-b14b-78c5b3febe96"
      },
      "source": [
        "movies[(movies.duration >= 200) | (movies.genre ==\"Drama\")]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
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
              "      <th>star_rating</th>\n",
              "      <th>title</th>\n",
              "      <th>content_rating</th>\n",
              "      <th>genre</th>\n",
              "      <th>duration</th>\n",
              "      <th>actors_list</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>9.1</td>\n",
              "      <td>The Godfather: Part II</td>\n",
              "      <td>R</td>\n",
              "      <td>Crime</td>\n",
              "      <td>200</td>\n",
              "      <td>[u'Al Pacino', u'Robert De Niro', u'Robert Duv...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>8.9</td>\n",
              "      <td>12 Angry Men</td>\n",
              "      <td>NOT RATED</td>\n",
              "      <td>Drama</td>\n",
              "      <td>96</td>\n",
              "      <td>[u'Henry Fonda', u'Lee J. Cobb', u'Martin Bals...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>8.9</td>\n",
              "      <td>The Lord of the Rings: The Return of the King</td>\n",
              "      <td>PG-13</td>\n",
              "      <td>Adventure</td>\n",
              "      <td>201</td>\n",
              "      <td>[u'Elijah Wood', u'Viggo Mortensen', u'Ian McK...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9</th>\n",
              "      <td>8.9</td>\n",
              "      <td>Fight Club</td>\n",
              "      <td>R</td>\n",
              "      <td>Drama</td>\n",
              "      <td>139</td>\n",
              "      <td>[u'Brad Pitt', u'Edward Norton', u'Helena Bonh...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>13</th>\n",
              "      <td>8.8</td>\n",
              "      <td>Forrest Gump</td>\n",
              "      <td>PG-13</td>\n",
              "      <td>Drama</td>\n",
              "      <td>142</td>\n",
              "      <td>[u'Tom Hanks', u'Robin Wright', u'Gary Sinise']</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>958</th>\n",
              "      <td>7.4</td>\n",
              "      <td>My Sister's Keeper</td>\n",
              "      <td>PG-13</td>\n",
              "      <td>Drama</td>\n",
              "      <td>109</td>\n",
              "      <td>[u'Cameron Diaz', u'Abigail Breslin', u'Alec B...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>968</th>\n",
              "      <td>7.4</td>\n",
              "      <td>The English Patient</td>\n",
              "      <td>R</td>\n",
              "      <td>Drama</td>\n",
              "      <td>162</td>\n",
              "      <td>[u'Ralph Fiennes', u'Juliette Binoche', u'Will...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>970</th>\n",
              "      <td>7.4</td>\n",
              "      <td>Wonder Boys</td>\n",
              "      <td>R</td>\n",
              "      <td>Drama</td>\n",
              "      <td>107</td>\n",
              "      <td>[u'Michael Douglas', u'Tobey Maguire', u'Franc...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>972</th>\n",
              "      <td>7.4</td>\n",
              "      <td>Blue Valentine</td>\n",
              "      <td>NC-17</td>\n",
              "      <td>Drama</td>\n",
              "      <td>112</td>\n",
              "      <td>[u'Ryan Gosling', u'Michelle Williams', u'John...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>973</th>\n",
              "      <td>7.4</td>\n",
              "      <td>The Cider House Rules</td>\n",
              "      <td>PG-13</td>\n",
              "      <td>Drama</td>\n",
              "      <td>126</td>\n",
              "      <td>[u'Tobey Maguire', u'Charlize Theron', u'Micha...</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>287 rows × 6 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "     star_rating  ...                                        actors_list\n",
              "2            9.1  ...  [u'Al Pacino', u'Robert De Niro', u'Robert Duv...\n",
              "5            8.9  ...  [u'Henry Fonda', u'Lee J. Cobb', u'Martin Bals...\n",
              "7            8.9  ...  [u'Elijah Wood', u'Viggo Mortensen', u'Ian McK...\n",
              "9            8.9  ...  [u'Brad Pitt', u'Edward Norton', u'Helena Bonh...\n",
              "13           8.8  ...    [u'Tom Hanks', u'Robin Wright', u'Gary Sinise']\n",
              "..           ...  ...                                                ...\n",
              "958          7.4  ...  [u'Cameron Diaz', u'Abigail Breslin', u'Alec B...\n",
              "968          7.4  ...  [u'Ralph Fiennes', u'Juliette Binoche', u'Will...\n",
              "970          7.4  ...  [u'Michael Douglas', u'Tobey Maguire', u'Franc...\n",
              "972          7.4  ...  [u'Ryan Gosling', u'Michelle Williams', u'John...\n",
              "973          7.4  ...  [u'Tobey Maguire', u'Charlize Theron', u'Micha...\n",
              "\n",
              "[287 rows x 6 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 51
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "gmWIil4jeFOD"
      },
      "source": [
        "**UYGULAMA:**\n",
        "web den bir veri seti bul ve bunla yukarıdaki işlemleri yap.\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 399
        },
        "id": "dmk_ycmzeVyX",
        "outputId": "21295c67-eca2-4bd5-d625-6ec15fc736ae"
      },
      "source": [
        "veri=pd.read_csv(\"https://raw.githubusercontent.com/Opensourcefordatascience/Data-sets/master/admission.csv\")\n",
        "veri"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
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
              "      <th>admit</th>\n",
              "      <th>gre</th>\n",
              "      <th>gpa</th>\n",
              "      <th>rank</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>0.0</td>\n",
              "      <td>380.0</td>\n",
              "      <td>3.61</td>\n",
              "      <td>3.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1.0</td>\n",
              "      <td>660.0</td>\n",
              "      <td>3.67</td>\n",
              "      <td>3.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>1.0</td>\n",
              "      <td>800.0</td>\n",
              "      <td>4.00</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1.0</td>\n",
              "      <td>640.0</td>\n",
              "      <td>3.19</td>\n",
              "      <td>4.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>0.0</td>\n",
              "      <td>520.0</td>\n",
              "      <td>2.93</td>\n",
              "      <td>4.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>395</th>\n",
              "      <td>0.0</td>\n",
              "      <td>620.0</td>\n",
              "      <td>4.00</td>\n",
              "      <td>2.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>396</th>\n",
              "      <td>0.0</td>\n",
              "      <td>560.0</td>\n",
              "      <td>3.04</td>\n",
              "      <td>3.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>397</th>\n",
              "      <td>0.0</td>\n",
              "      <td>460.0</td>\n",
              "      <td>2.63</td>\n",
              "      <td>2.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>398</th>\n",
              "      <td>0.0</td>\n",
              "      <td>700.0</td>\n",
              "      <td>3.65</td>\n",
              "      <td>2.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>399</th>\n",
              "      <td>0.0</td>\n",
              "      <td>600.0</td>\n",
              "      <td>3.89</td>\n",
              "      <td>3.0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>400 rows × 4 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "     admit    gre   gpa  rank\n",
              "0      0.0  380.0  3.61   3.0\n",
              "1      1.0  660.0  3.67   3.0\n",
              "2      1.0  800.0  4.00   1.0\n",
              "3      1.0  640.0  3.19   4.0\n",
              "4      0.0  520.0  2.93   4.0\n",
              "..     ...    ...   ...   ...\n",
              "395    0.0  620.0  4.00   2.0\n",
              "396    0.0  560.0  3.04   3.0\n",
              "397    0.0  460.0  2.63   2.0\n",
              "398    0.0  700.0  3.65   2.0\n",
              "399    0.0  600.0  3.89   3.0\n",
              "\n",
              "[400 rows x 4 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 101
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 194
        },
        "id": "akMG1PC9f71m",
        "outputId": "34192aa2-19c0-41e5-9daf-ffd3985a97bf"
      },
      "source": [
        "veri.head()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
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
              "      <th>admit</th>\n",
              "      <th>gre</th>\n",
              "      <th>gpa</th>\n",
              "      <th>rank</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>0.0</td>\n",
              "      <td>380.0</td>\n",
              "      <td>3.61</td>\n",
              "      <td>3.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1.0</td>\n",
              "      <td>660.0</td>\n",
              "      <td>3.67</td>\n",
              "      <td>3.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>1.0</td>\n",
              "      <td>800.0</td>\n",
              "      <td>4.00</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1.0</td>\n",
              "      <td>640.0</td>\n",
              "      <td>3.19</td>\n",
              "      <td>4.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>0.0</td>\n",
              "      <td>520.0</td>\n",
              "      <td>2.93</td>\n",
              "      <td>4.0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   admit    gre   gpa  rank\n",
              "0    0.0  380.0  3.61   3.0\n",
              "1    1.0  660.0  3.67   3.0\n",
              "2    1.0  800.0  4.00   1.0\n",
              "3    1.0  640.0  3.19   4.0\n",
              "4    0.0  520.0  2.93   4.0"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 102
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "V8LIRhP9gxUW",
        "outputId": "c539436b-324f-4fa9-c871-f7ee0432421d"
      },
      "source": [
        "veri.gre"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0      380.0\n",
              "1      660.0\n",
              "2      800.0\n",
              "3      640.0\n",
              "4      520.0\n",
              "       ...  \n",
              "395    620.0\n",
              "396    560.0\n",
              "397    460.0\n",
              "398    700.0\n",
              "399    600.0\n",
              "Name: gre, Length: 400, dtype: float64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 103
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mkAT18BEhfPP",
        "outputId": "36c4be5b-3f78-4fbc-cc5a-380c214e1995"
      },
      "source": [
        "veri.shape"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(400, 4)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 104
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 282
        },
        "id": "Wzsnj4JfhfCP",
        "outputId": "81be097b-c30f-4c28-e5d8-0d14c0a8db91"
      },
      "source": [
        "veri.describe()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
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
              "      <th>admit</th>\n",
              "      <th>gre</th>\n",
              "      <th>gpa</th>\n",
              "      <th>rank</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>400.000000</td>\n",
              "      <td>400.000000</td>\n",
              "      <td>400.000000</td>\n",
              "      <td>400.00000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>0.317500</td>\n",
              "      <td>587.700000</td>\n",
              "      <td>3.389900</td>\n",
              "      <td>2.48500</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>0.466087</td>\n",
              "      <td>115.516536</td>\n",
              "      <td>0.380567</td>\n",
              "      <td>0.94446</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>0.000000</td>\n",
              "      <td>220.000000</td>\n",
              "      <td>2.260000</td>\n",
              "      <td>1.00000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>0.000000</td>\n",
              "      <td>520.000000</td>\n",
              "      <td>3.130000</td>\n",
              "      <td>2.00000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>0.000000</td>\n",
              "      <td>580.000000</td>\n",
              "      <td>3.395000</td>\n",
              "      <td>2.00000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>1.000000</td>\n",
              "      <td>660.000000</td>\n",
              "      <td>3.670000</td>\n",
              "      <td>3.00000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>1.000000</td>\n",
              "      <td>800.000000</td>\n",
              "      <td>4.000000</td>\n",
              "      <td>4.00000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "            admit         gre         gpa       rank\n",
              "count  400.000000  400.000000  400.000000  400.00000\n",
              "mean     0.317500  587.700000    3.389900    2.48500\n",
              "std      0.466087  115.516536    0.380567    0.94446\n",
              "min      0.000000  220.000000    2.260000    1.00000\n",
              "25%      0.000000  520.000000    3.130000    2.00000\n",
              "50%      0.000000  580.000000    3.395000    2.00000\n",
              "75%      1.000000  660.000000    3.670000    3.00000\n",
              "max      1.000000  800.000000    4.000000    4.00000"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 105
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "G43ISmf2hotu",
        "outputId": "012fdd77-fa94-4724-f00b-f6e1a6d77603"
      },
      "source": [
        "type(veri)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "pandas.core.frame.DataFrame"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 106
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kTVDf6W2hqyS",
        "outputId": "1e2f3a6a-a7e3-47c8-e98c-4920dd8a4af5"
      },
      "source": [
        "veri.columns"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Index(['admit', 'gre', 'gpa', 'rank'], dtype='object')"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 107
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7CxSqQTgh1f6",
        "outputId": "8465bf35-9223-4ac9-d221-0c0f95b671bf"
      },
      "source": [
        "veri.columns=veri.columns.str.replace(\" \" , \"_\")\n",
        "veri.columns"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Index(['admit', 'gre', 'gpa', 'rank'], dtype='object')"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 109
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NlQbmkheiB9a",
        "outputId": "6cd8b0e1-6840-45b2-cadc-ee1130356ba9"
      },
      "source": [
        "veri[\"rank\"].sort_values()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "126    1.0\n",
              "165    1.0\n",
              "357    1.0\n",
              "306    1.0\n",
              "360    1.0\n",
              "      ... \n",
              "317    4.0\n",
              "314    4.0\n",
              "313    4.0\n",
              "254    4.0\n",
              "199    4.0\n",
              "Name: rank, Length: 400, dtype: float64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 110
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "z4OHHLuMiK2G",
        "outputId": "96cd36d1-fc92-468f-da54-0f846feb2ba9"
      },
      "source": [
        "veri[\"gre\"].sort_values(ascending=False)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "293    800.0\n",
              "286    800.0\n",
              "369    800.0\n",
              "25     800.0\n",
              "33     800.0\n",
              "       ...  \n",
              "316    340.0\n",
              "315    300.0\n",
              "71     300.0\n",
              "179    300.0\n",
              "304    220.0\n",
              "Name: gre, Length: 400, dtype: float64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 111
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 47
        },
        "id": "DoLH1IEAiUOW",
        "outputId": "96a85aae-81b2-45dc-a56a-568352c767f8"
      },
      "source": [
        "veri[9:8]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
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
              "      <th>admit</th>\n",
              "      <th>gre</th>\n",
              "      <th>gpa</th>\n",
              "      <th>rank</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "Empty DataFrame\n",
              "Columns: [admit, gre, gpa, rank]\n",
              "Index: []"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 112
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 135
        },
        "id": "BH-s254um3TK",
        "outputId": "aedd5eec-1544-405a-affc-18a84580f6f5"
      },
      "source": [
        "veri.iloc[1:4, 1:3]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
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
              "      <th>gre</th>\n",
              "      <th>gpa</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>660.0</td>\n",
              "      <td>3.67</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>800.0</td>\n",
              "      <td>4.00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>640.0</td>\n",
              "      <td>3.19</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "     gre   gpa\n",
              "1  660.0  3.67\n",
              "2  800.0  4.00\n",
              "3  640.0  3.19"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 113
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 399
        },
        "id": "2WCNy79gm3Rl",
        "outputId": "e0d200af-ac04-4b88-e53e-a341027059e7"
      },
      "source": [
        "veri[veri.gre >= 500.0]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
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
              "      <th>admit</th>\n",
              "      <th>gre</th>\n",
              "      <th>gpa</th>\n",
              "      <th>rank</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1.0</td>\n",
              "      <td>660.0</td>\n",
              "      <td>3.67</td>\n",
              "      <td>3.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>1.0</td>\n",
              "      <td>800.0</td>\n",
              "      <td>4.00</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1.0</td>\n",
              "      <td>640.0</td>\n",
              "      <td>3.19</td>\n",
              "      <td>4.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>0.0</td>\n",
              "      <td>520.0</td>\n",
              "      <td>2.93</td>\n",
              "      <td>4.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>1.0</td>\n",
              "      <td>760.0</td>\n",
              "      <td>3.00</td>\n",
              "      <td>2.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>393</th>\n",
              "      <td>1.0</td>\n",
              "      <td>620.0</td>\n",
              "      <td>3.75</td>\n",
              "      <td>2.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>395</th>\n",
              "      <td>0.0</td>\n",
              "      <td>620.0</td>\n",
              "      <td>4.00</td>\n",
              "      <td>2.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>396</th>\n",
              "      <td>0.0</td>\n",
              "      <td>560.0</td>\n",
              "      <td>3.04</td>\n",
              "      <td>3.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>398</th>\n",
              "      <td>0.0</td>\n",
              "      <td>700.0</td>\n",
              "      <td>3.65</td>\n",
              "      <td>2.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>399</th>\n",
              "      <td>0.0</td>\n",
              "      <td>600.0</td>\n",
              "      <td>3.89</td>\n",
              "      <td>3.0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>322 rows × 4 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "     admit    gre   gpa  rank\n",
              "1      1.0  660.0  3.67   3.0\n",
              "2      1.0  800.0  4.00   1.0\n",
              "3      1.0  640.0  3.19   4.0\n",
              "4      0.0  520.0  2.93   4.0\n",
              "5      1.0  760.0  3.00   2.0\n",
              "..     ...    ...   ...   ...\n",
              "393    1.0  620.0  3.75   2.0\n",
              "395    0.0  620.0  4.00   2.0\n",
              "396    0.0  560.0  3.04   3.0\n",
              "398    0.0  700.0  3.65   2.0\n",
              "399    0.0  600.0  3.89   3.0\n",
              "\n",
              "[322 rows x 4 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 121
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 839
        },
        "id": "fXfj6gbhm3Oo",
        "outputId": "0f592369-2db0-4152-9493-4ee0c5c6aee6"
      },
      "source": [
        "veri[(veri.gre >= 500.0) &  (veri.gpa >= 4.0) ] "
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
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
              "      <th>admit</th>\n",
              "      <th>gre</th>\n",
              "      <th>gpa</th>\n",
              "      <th>rank</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>1.0</td>\n",
              "      <td>800.0</td>\n",
              "      <td>4.0</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>10</th>\n",
              "      <td>0.0</td>\n",
              "      <td>800.0</td>\n",
              "      <td>4.0</td>\n",
              "      <td>4.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>12</th>\n",
              "      <td>1.0</td>\n",
              "      <td>760.0</td>\n",
              "      <td>4.0</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>14</th>\n",
              "      <td>1.0</td>\n",
              "      <td>700.0</td>\n",
              "      <td>4.0</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>33</th>\n",
              "      <td>1.0</td>\n",
              "      <td>800.0</td>\n",
              "      <td>4.0</td>\n",
              "      <td>3.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>55</th>\n",
              "      <td>1.0</td>\n",
              "      <td>740.0</td>\n",
              "      <td>4.0</td>\n",
              "      <td>3.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>64</th>\n",
              "      <td>0.0</td>\n",
              "      <td>580.0</td>\n",
              "      <td>4.0</td>\n",
              "      <td>3.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>70</th>\n",
              "      <td>0.0</td>\n",
              "      <td>640.0</td>\n",
              "      <td>4.0</td>\n",
              "      <td>3.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>73</th>\n",
              "      <td>0.0</td>\n",
              "      <td>580.0</td>\n",
              "      <td>4.0</td>\n",
              "      <td>2.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75</th>\n",
              "      <td>0.0</td>\n",
              "      <td>720.0</td>\n",
              "      <td>4.0</td>\n",
              "      <td>3.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>77</th>\n",
              "      <td>1.0</td>\n",
              "      <td>800.0</td>\n",
              "      <td>4.0</td>\n",
              "      <td>3.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>79</th>\n",
              "      <td>1.0</td>\n",
              "      <td>620.0</td>\n",
              "      <td>4.0</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>89</th>\n",
              "      <td>1.0</td>\n",
              "      <td>660.0</td>\n",
              "      <td>4.0</td>\n",
              "      <td>2.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>137</th>\n",
              "      <td>0.0</td>\n",
              "      <td>700.0</td>\n",
              "      <td>4.0</td>\n",
              "      <td>3.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>165</th>\n",
              "      <td>0.0</td>\n",
              "      <td>700.0</td>\n",
              "      <td>4.0</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>168</th>\n",
              "      <td>0.0</td>\n",
              "      <td>500.0</td>\n",
              "      <td>4.0</td>\n",
              "      <td>3.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>182</th>\n",
              "      <td>0.0</td>\n",
              "      <td>700.0</td>\n",
              "      <td>4.0</td>\n",
              "      <td>2.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>202</th>\n",
              "      <td>1.0</td>\n",
              "      <td>700.0</td>\n",
              "      <td>4.0</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>252</th>\n",
              "      <td>1.0</td>\n",
              "      <td>520.0</td>\n",
              "      <td>4.0</td>\n",
              "      <td>2.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>310</th>\n",
              "      <td>0.0</td>\n",
              "      <td>560.0</td>\n",
              "      <td>4.0</td>\n",
              "      <td>3.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>330</th>\n",
              "      <td>0.0</td>\n",
              "      <td>740.0</td>\n",
              "      <td>4.0</td>\n",
              "      <td>3.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>350</th>\n",
              "      <td>1.0</td>\n",
              "      <td>780.0</td>\n",
              "      <td>4.0</td>\n",
              "      <td>2.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>360</th>\n",
              "      <td>1.0</td>\n",
              "      <td>520.0</td>\n",
              "      <td>4.0</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>368</th>\n",
              "      <td>0.0</td>\n",
              "      <td>580.0</td>\n",
              "      <td>4.0</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>377</th>\n",
              "      <td>1.0</td>\n",
              "      <td>800.0</td>\n",
              "      <td>4.0</td>\n",
              "      <td>2.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>383</th>\n",
              "      <td>0.0</td>\n",
              "      <td>660.0</td>\n",
              "      <td>4.0</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>395</th>\n",
              "      <td>0.0</td>\n",
              "      <td>620.0</td>\n",
              "      <td>4.0</td>\n",
              "      <td>2.0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "     admit    gre  gpa  rank\n",
              "2      1.0  800.0  4.0   1.0\n",
              "10     0.0  800.0  4.0   4.0\n",
              "12     1.0  760.0  4.0   1.0\n",
              "14     1.0  700.0  4.0   1.0\n",
              "33     1.0  800.0  4.0   3.0\n",
              "55     1.0  740.0  4.0   3.0\n",
              "64     0.0  580.0  4.0   3.0\n",
              "70     0.0  640.0  4.0   3.0\n",
              "73     0.0  580.0  4.0   2.0\n",
              "75     0.0  720.0  4.0   3.0\n",
              "77     1.0  800.0  4.0   3.0\n",
              "79     1.0  620.0  4.0   1.0\n",
              "89     1.0  660.0  4.0   2.0\n",
              "137    0.0  700.0  4.0   3.0\n",
              "165    0.0  700.0  4.0   1.0\n",
              "168    0.0  500.0  4.0   3.0\n",
              "182    0.0  700.0  4.0   2.0\n",
              "202    1.0  700.0  4.0   1.0\n",
              "252    1.0  520.0  4.0   2.0\n",
              "310    0.0  560.0  4.0   3.0\n",
              "330    0.0  740.0  4.0   3.0\n",
              "350    1.0  780.0  4.0   2.0\n",
              "360    1.0  520.0  4.0   1.0\n",
              "368    0.0  580.0  4.0   1.0\n",
              "377    1.0  800.0  4.0   2.0\n",
              "383    0.0  660.0  4.0   1.0\n",
              "395    0.0  620.0  4.0   2.0"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 124
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "jFc6pG6-ifU-"
      },
      "source": [
        "***UYGULAMA SONRASI YENİ KONU:***"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "cwJNio3pii42"
      },
      "source": [
        "import matplotlib.pyplot as plt"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "QC9nQriHi5HJ"
      },
      "source": [
        "x = [1,8,12,15,16,18]\n",
        "y = [50,42,30,78,89,75]"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 297
        },
        "id": "MAAxgjy9i5Fb",
        "outputId": "ff757eb5-8103-43a1-e645-8a10888f95aa"
      },
      "source": [
        "plt.plot(x,y)\n",
        "plt.xlabel(\"X ekseni\")\n",
        "plt.ylabel(\"Y ekseni\")"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Text(0, 0.5, 'Y ekseni')"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 127
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAX4AAAEGCAYAAABiq/5QAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAgAElEQVR4nO3dd5hU9fn38fe9jaUsZWFpAlIFpCOKFSkWBKPGqLElaooxlkSNJjHtl/yePE9iNDEmlkhiDEnUGI0tLlYE7CJ1FxWk1wWWsnTYdj9/nLO44AKL7Jn6eV3XXrNz5pyZm9nhnjOf+Z7vMXdHRETSR0a8CxARkdhS4xcRSTNq/CIiaUaNX0Qkzajxi4ikmax4F1Afbdq08a5du8a7DBGRpDJz5swN7l6w//KkaPxdu3ZlxowZ8S5DRCSpmNnyupYr6hERSTNq/CIiaSbSxm9m3zWzeWb2oZndHC7LN7NXzWxheNkqyhpERGRfkTV+M+sPfBM4ARgEnGtmPYEfApPdvRcwObwuIiIxEuUef1/gfXff6e6VwDTgQuB8YGK4zkTggghrEBGR/UTZ+OcBp5lZazNrAowDOgPt3L0kXGct0K6ujc3sWjObYWYzSktLIyxTRCS9RNb43f1j4E7gFeAlYA5Qtd86DtQ5Pai7T3D3Ye4+rKDgM8NQRUTkc4r0y113f9jdj3P3EcBm4BNgnZl1AAgv10dZg4hIfVRVO0/PWkXZzvJ4lxK5qEf1tA0vuxDk+48BzwNXhatcBTwXZQ0iIvXx3JzV3Prvudz42GyqqlP7PCVRj+P/j5l9BPwXuMHdy4BfA2ea2ULgjPC6iEjcVFU7909ZRPPcLN5atIE/TF4Y75IiFemUDe5+Wh3LNgJjonxcEZHD8dK8tSwu3cEfLxvC1AWl/OH1hRx3dCtGHJOa3y/qyF0RSWvV1c4fX19I94KmjBvQgV9e0J9j2uZx8xNzKNmyK97lRUKNX0TS2uT565m/dhs3jupJZobROCeTB64cyp6KKm54dBYVVdXxLrHBqfGLSNpyd+57fSGd8xtz3qCOe5f3KGjGnRcNZNaKMn794vw4VhgNNX4RSVtvLNzA3FVbuH5kT7Iy922H5w7syNUnd+Xht5by0rySA9xDclLjF5G05O78cfJCOrTI5UtDO9W5zo/G9WVQ55bc/mQRyzbsiHGF0VHjF5G09N6STcxYvpnrTu9BTlbdrTAnK4P7Lx9CRobx7Udnsbuiqs71ko0av4ikpfumLKRNs0Z8+fjOB12vU6sm/P7Lg/m4ZCv/89yHMaouWmr8IpJ2Zi7fzNuLNvKtEd3Jzc485Pqj+rTlhlE9eGLGSp6auSoGFUZLjV9E0s59ry+kVZNsLh/epd7b3HLGMZzUvTU/ebaY+Wu3Rlhd9NT4RSStzFu9hSkLSvnGad1p2qj+kxdkZWZw72WDycvN5vp/zmLb7ooIq4yWGr+IpJX7Xl9EXm4WXznp6MPetm1eLvddNoTlm3byw6eLCWaWTz5q/CKSNhas3cZLH67lmpO70jw3+3Pdx/DurbntrN4UFpUw8Z1lDVtgjKjxi0jauH/KIprmZHLNKd2O6H6+NaI7Z/Rty/+d9DGzV2xuoOpiR41fRNLCktLtvFC0hitPOppWTXOO6L4yMozfXjyYds1zueHRWWzekVwnb1HjF5G08MDUxeRkZfCNU7s3yP21aJLNA1cMZcP2cm759xyqk+jkLWr8IpLyVm7ayTOzV3PZCV0oyGvUYPc7sFNLfvqFY5m6oJQHpy1usPuNmhq/iKS8B6ctJtOMb43o0eD3feXwLpw3qCO/fWUB7yze0OD3HwU1fhFJaSVbdvHUjFVcPKwT7VvkNvj9mxm/unAA3Qua8Z3HZ7Nu6+4Gf4yGpsYvIiltwhtLqHLnutMbfm+/RtNGWTx4xVB27KnipsdnU5ngJ29R4xeRlFW6bQ+Pvb+CLw45is75TSJ9rF7t8vjVhQOYvnQTd7/ySaSPdaTU+EUkZf3lrSVUVFVz/cjo9vZru2DIUVw+vAt/mraYVz9aF5PH/DzU+EUkJW3eUc4/3l3OuQM70r2gWcwe92fnHkv/o5rzvX/PYeWmnTF73MOhxi8iKemRt5eys7yKG0b1jOnj5mZn8sDlx+HA9Ql68hY1fhFJOVt3V/DIO8sY2689vdvnxfzxu7Ruwm8vHkTx6i38svCjmD/+oUTa+M3sFjP70MzmmdnjZpZrZt3M7H0zW2RmT5jZkR07LSKyn7+/s4xtuyu5cXRs9/ZrO6tfe741ojv/fG8Fz81ZHbc66hJZ4zezo4DvAMPcvT+QCVwK3Anc4+49gc3A16OqQUTSz449lTz81lJG92lL/6NaxLWW287uzfFdW3HH08UsWr8trrXUFnXUkwU0NrMsoAlQAowGngpvnwhcEHENIpJGHn1/OZt3VsQ8269LdmYG910+lCY5mVz3z1ns2FMZ75KACBu/u68G7gZWEDT8LcBMoMzda/71q4Cj6trezK41sxlmNqO0tDSqMkUkheyuqGLCG0s5pWdrjju6VbzLAaBd81zuvXQIi0u38+NnEuPkLVFGPa2A84FuQEegKTC2vtu7+wR3H+buwwoKCiKqUkRSyRMfrGTD9j3cNLpXvEvZxyk923DrGcfw7Jw1PDZ9RbzLiTTqOQNY6u6l7l4BPA2cArQMox+ATkBifeshIklpT2UVf5q2mOO7tmJ4t/x4l/MZN4zqyenHFPCL5z+ieNWWuNYSZeNfAZxoZk3MzIAxwEfAFOCicJ2rgOcirEFE0sTTs1ZTsmU3N47uRdByEktGhnHPlwfTulkO1z82ky0743ey9igz/vcJvsSdBRSHjzUB+AFwq5ktAloDD0dVg4ikh8qqah6YuohBnVowolebeJdzQPlNc7j/iqGUlO3me0/OjVveH+moHnf/H3fv4+793f0r7r7H3Ze4+wnu3tPdL3b3PVHWICKp77k5a1i5aVfC7u3XNrRLK340ri+vfbyOCW8siUsNOnJXRJJadbVz/9RF9O3QnDP6to13OfVyzSldGTegPb95eQHTl26K+eOr8YtIUpu5YjNLSnfwzdO6Jfzefg0z484vDaRLfhNufGwWpdtiG3yo8YtIUissKiEnK4Oz+rWPdymHJS83OFn7ll0VfPdfs6mK4cna1fhFJGlVVzsvzith5DEFNGuUdegNEkzfDs35Pxf0553FG/n9a7E7eYsav4gkrZkrNrNu6x7GD+wQ71I+t0uGdebi4zrxx9cXMXXB+pg8phq/iCStmphnTN928S7liPzv+f3p0z6PW56Yw+qyXZE/nhq/iCSl6mpnUnEJo3onZ8xTW+OcTB688jgqqpwbHp1FeWW0J2tX4xeRpDRj+WbWb9vDuAHJG/PU1q1NU35z0UDmrCzjVy9+HOljqfGLSFKaVFxCoxSIeWobN6AD15zSlUfeXkZhUUlkj6PGLyJJpybmGZkCMc/+7jinL0O6tOQH/yliSen2SB5DjV9Ekk5NzDN+YMd4l9LgcrIyuP/yoWRnGtc/Ootd5Q1/snY1fhFJOoVFa4KYp09yTNFwuDq2bMw9Xx7Mhu3lLNu4o8HvP7U+I4lIyquqdl6ct5ZRvdvSNMVintpG9m7LG98fSZOchv83ao9fRJLKjGWbgtE8SXzQVn1F0fRBjV9Eksze0TwpGvPEghq/iCSNqmpnUhrEPFFT4xeRpDFj2SZKtyX33DyJQI1fRJJGYRjzjFbMc0TU+EUkKdSM5hndRzHPkVLjF5Gk8EEY86TK3DzxpMYvIklhUnEJudmKeRqCGr+IJLyqamdSsUbzNBQ1fhFJeB8s28SG7RrN01DU+EUk4RUWKeZpSGr8IpLQao/miWoKg3QTWeM3s95mNqfWz1Yzu9nM8s3sVTNbGF62iqoGEUl+05cGMY9G8zScyBq/uy9w98HuPhg4DtgJPAP8EJjs7r2AyeF1EZE6aTRPw4tV1DMGWOzuy4HzgYnh8onABTGqQUSSjGKeaMSq8V8KPB7+3s7da04muRao84SZZnatmc0wsxmlpaWxqFFEEkxNzDN+QOqdaSueIm/8ZpYDnAc8uf9t7u6A17Wdu09w92HuPqygoCDiKkUkERUWryE3O4NRfdQDGlIs9vjPAWa5+7rw+joz6wAQXq6PQQ0ikmSqqp2X5q1lTJ92inkaWCwa/2V8GvMAPA9cFf5+FfBcDGoQkSTz/tKNbNhertE8EYi08ZtZU+BM4Olai38NnGlmC4EzwusiIvuYVFxC4+xMxTwRiPTzk7vvAFrvt2wjwSgfEZE61cQ8Gs0TDR25KyIJpybm0dw80VDjF5GEU1gUxjy9ddBWFNT4RSShVFZV8/KHaxndty2NczLjXU5KUuMXkYQSHLRVzniN5omMGr+IJJTCYsU8UVPjF5GEUVlVHYzmUcwTKTV+EUkY05duYuOOcs5VzBMpNX4RSRgvhDHPSMU8kVLjF5GEUFlVzcvz1jJGMU/k1PhFJCG8H8Y8Gs0TPTV+EUkIhcUlNMlRzBMLB5wEw8x+7+43m9l/qWPOfHc/L9LKRCRt7B3N00cxTywcbPajf4SXd8eiEBFJX+8v3cSmHeWcq7l5YuKAjd/dZ4aX02JXjoikoxeKFPPE0iHnOzWzU4CfA0eH6xvBWRO7R1uaiKSDmrl5xvRtR262Yp5YqM9E1w8DtwAzgapoyxGRdPPekiDmGT+gfbxLSRv1afxb3P3FyCsRkbSk0TyxV5/GP8XM7iI4feKemoXuPiuyqkQkLSjmiY/6NP7h4eWwWsscGN3w5YhIOvk05tFonlg6ZON391GxKERE0k9h8Rqa5mQysrdOqB5Lhzxy18zamdnDZvZieP1YM/t69KWJSCqrOWhLMU/s1WfKhr8BLwMdw+ufADdHVZCIpId3l2xk884Kxinmibn6NP427v5voBrA3SvRsE4ROUKTiksU88RJfRr/DjNrTThfj5mdCGyJtCoRSWkVinniqj6jem4Fngd6mNnbQAFwUX3u3MxaAn8B+hO8cXwNWAA8AXQFlgGXuPvmwy1cRJLXe2HMM15z88TFIff4w/H6pwMnA98C+rl7UT3v/17gJXfvAwwCPgZ+CEx2917A5PC6iKSRwqIg5jn9GMU88VCfUT0XA43d/UPgAuAJMxtaj+1aACMIpnzA3cvdvQw4H5gYrjYxvE8RSRMV4UFbZxyrmCde6pPx/9Tdt5nZqcAYgkb+YD226waUAo+Y2Wwz+4uZNQXauXtJuM5aoF1dG5vZtWY2w8xmlJaW1uPhRCQZvLtYo3nirT6Nv2YEz3jgz+5eCOTUY7ssYCjwoLsPAXawX6zj7k4dJ3kJb5vg7sPcfVhBgT4OiqSKmtE8innipz6Nf7WZPQR8GZhkZo3qud0qYJW7vx9ef4rgjWCdmXUACC/XH37ZIpKMKqqqeUkxT9zVp4FfQnAA19lhRp8P3H6ojdx9LbDSzHqHi8YAHxGMELoqXHYV8NzhFi0iyendxRsp21mhuXnirD7DOS9z94drrrh7iZl9F3ilHtveBDxqZjnAEuAagjebf4fTPiwneGMRkTRQWFRCs0ZZjFDME1f1afxfMrPd7v4ogJndD+TW587dfQ77zupZY0z9SxSRVFBRVc3LH63ljL5tFfPEWb0aP/C8mVUDY4Eyd9ckbSJyWN4JYx6N5om/AzZ+M8uvdfUbwLPA28AvzCzf3TdFXZyIpI5JinkSxsH2+GcSDLW0Wpfjwx8HdLJ1EakXxTyJ5YCN3927xbIQEUldNTHP+IEdD72yRK4+UzY0MbOfmNmE8HovMzs3+tJEJFUUFq2hWaMsTuvVJt6lCPUbx/8IUE4wSRvAauCXkVUkIiklmJtnHWfqoK2EUZ/G38PdfwNUALj7ToK8X0TkkN5etIEtuzSaJ5HUp/GXm1ljPj0RSw9gT6RViUjKmFRcQp5inoRSn3H8/wO8BHQ2s0eBU4CroyxKRFJDTcyjuXkSyyEbv7u/amazgBMJIp7vuvuGyCsTkaRXE/Nobp7EUp89ftx9I1AYcS0ikmIKi8KY5xjFPImkPhm/iMhhK6+s5pWPgtE8jbIU8ySSAzZ+M5tkZl1jV4qIpJK3F2s0T6I62B7/I8ArZvZjM8uOVUEikhomKeZJWAebsuFJM3sR+Ckww8z+AVTXuv13MahPRJJQeWVwQnXFPInpUF/ulhOcK7cRkEetxi8iciBvL97A1t2VjB+omCcRHWxa5rHA7whOlTg0PGJXROSQakbznKqDthLSwfb4fwxc7O4fxqoYEUl+5ZXVvPLhWs7sp5gnUR0s4z8tloWISGp4e1EY82g0T8LSOH4RaVCFxSXk5SrmSWRq/CLSYPbGPBrNk9DU+EWkwdTEPOdqNE9CU+MXkQbzQlEY8/TUCdUTmRq/iDSIYG6etZx1bHtystRaEpn+OiLSIN5aVMq23ZWMH9g+3qXIIdRrWubPy8yWAduAKqDS3YeZWT7wBNAVWAZc4u6bo6xDRKJXWLRWMU+SiMUe/yh3H+zuw8LrPwQmu3svYHJ4XUSS2J7KKsU8SSTSPf4DOB8YGf4+EZgK/CCKB7rj6SIWrd/O4M4tGdS5JYM7t+Solo0x07niRRrS24s2sE2jeZJG1I3fCaZ2duAhd58AtHP3kvD2tUC7ujY0s2uBawG6dOnyuR68S35TFqzdxsR3l1P+5lIA2jRrxODOLRncuQWDO7diYOcWNM/VrNMiR+KFohKa52ZxSk8dtJUMom78p7r7ajNrC7xqZvNr3+juHr4pfEb4JjEBYNiwYXWucyjfHtmDb4/sQXllNQvWbmPOys3MXlnG3JVlvPbxOgDMoEdBMwZ1asngLi0Z0rklvdvnkZ2pj6si9bGnsopXP1rH2f0U8ySLSBu/u68OL9eb2TPACcA6M+vg7iVm1gFYH2UNADlZGQzo1IIBnVrwlZOCZVt2VVC0qow5K8qYu6qMaZ+s5z+zVgHQKCuD/ke1CD8ZBD+dWikiEqnLWwuDmEdz8ySPyBq/mTUFMtx9W/j7WcD/EkzzfBXw6/DyuahqOJgWjbM5rVcBp/UKRiC4O6s272JO+Ilgzsoy/vnech5+qyYiygk+FYTfFwzq3JIWjRURiRQWK+ZJNlHu8bcDngn3krOAx9z9JTP7APi3mX0dWA5cEmEN9WZmdM5vQuf8JnxhUEcAKqpqIqKyvT+T53/6AaV7QdN9PhX0ad9cH3UlreyprOLVD9dxdn/FPMkkssbv7kuAQXUs3wiMiepxG1J2ZhD59D+qBVeeeDQAW3dXULRyC3NXlTF7RRlvfLKBp2etBoJIqX/H5ntHEA3p3IrO+YqIJHW9tXAD2/boTFvJJh7DOZNa89xsTu3VZu+Us+7O6rJdzF25hTkrNzNnZRmPT1/BI28vAyC/aQ6DOgUjiAZ3acngTi1p0UQRkaSGwprRPD0U8yQTNf4jZGZ0atWETq2a7N3rqaiq5pN1YUS0IoiIpn5Siodjk7q12Tci6ttBEZEkn5rRPGMV8yQdNf4IZGdm0K9jC/p1bMEVw4OIaNvuCopXbWF2+F3BW4s28MzsMCLKzODYjs2DeKhLSwZ1asnRrZsoIpKE9uYnQcwzTjFP0lHjj5G83GxO7tmGk3t+GhGVbNm9zxfHT3ywkr+9swyAVk2y935XMKhzEBG1apoTx3+ByL4mFZfQonG2Yp4kpMYfJ2ZGx5aN6diyMePC8c+VVdV8sm77PkNKp32ycG9E1LV1k32mnzi2Y3Od5UjiQjFPclPjTyBZYeRzbMfmXD48mKZi+55KilaV7f3y+N0lG3l2zhogiIj6dmzO4E4tgi+OO7eiqyIiiYGamEejeZKTGn+Ca9Yoi5N7tOHkWh+nS7bsYu7KsuD7ghVlPDlzFRPfXQ4EB6Z9Opw0+HSQr4hIGlhhTcyjg7aSkhp/EurQojEdWjRmbP9gb6uq2lm4ftveEURzVpZx3+sLqQ4joi75TfaOIBrUuSX9OjYnN1sRkXw+uyuqeO2jdZwzoL3mtEpSavwpIDPD6NO+OX3aN+fSE4KIaMeeSopXb9k7pPSDZZt4fm4QEWVnGn07BKOIaian69a6KRkZiojk0N4MD9oap7l5kpYaf4pq2iiLE7u35sTurfcuW7d1N7PDTwVzV5bxn5mr+HsYETXPzdobEdX8tG7WKF7lSwKbpJgn6anxp5F2zXMZ2789Y/sH50StqnYWrd8eHnEcfDq4f8qivRFR5/zGeyemG9KlJf06tlBElOZ2VwSjecYp5klqavxpLDPD6N0+j97t8/jy8cGyneWVFK8K5iKas7KMWcs380JRcN6crAyjT4e88BNBKwZ3bkn3NoqI0smbCzewfU8l4wd2jHcpcgTU+GUfTXKyGN69NcNrRUTrt+57oNmzs9fwz/dWAJCXm7X3U0HNl8cFeYqIUlVh0RpaNsnm5B6tD72yJCw1fjmkts1zOatfe87q92lEtKR0+97pJ+asKOPBaYupCjOio1o23jsh3eAuLenfsQWNcxQRJbvdFVW89vF6xg/ooJgnyanxy2HLzDB6tcujV7s8LhnWGYBd5VXMW7Pl0yGlK8ooDCOiYNRR3j7HF/QoaKaIKMm88Ukp2zU3T0pQ45cG0Tgnk+O75nN81/y9y9Zv2733iOO5K7fw3zlreOz9ICJq1iiLgZ1qnd6yS0va5uXGq3yph8LiEsU8KUKNXyLTNi+XM4/N5cxj2wFQXe0s2bCd2eF5juesLGPCG0uoDCOiji1yw6kngi+P+x/VnCY5eokmgpqDts4d2FExTwrQ/yqJmYwMo2fbPHq2zePiMCLaXVHFvJoDzcKfScVrgSAiOqZd3j7TT/Rs24xMRUQxN+2TUnaUV2lunhShxi9xlZudybCu+QyrFRGVbttD0apP3wheKFrD49M/jYgGHBVMSjeoU3B8QbvmioiiNimMeU5SzJMS1Pgl4RTkNWJM33aM6ftpRLR044595iL6c62IqEOL3H2mqx7YqYUiogZUE/N8YZBinlSh/x2S8DIyjB4FzehR0IwvHdcJCJrRh2u27n0jmLuyjBfnBRFRo6wMvnlad64b2YNmjfQSP1I1MY/m5kkd+l8hSSk3O5Pjjm7FcUe32rts4/Y9zF0VHGB235RF/OuDlXzvrGO4ZFhnfS9wBAqLSmilmCel6HObpIzWzRoxuk87/nDZEJ65/mSObt2EO54uZvwf3uTNhaXxLi8p7a6oYvLH6zi7n+bmSSX6S0pKGtKlFU9ddxIPXDGUHeWVfOXh6VzzyHQWrtsW79KSytQFGs2TiiJv/GaWaWazzeyF8Ho3M3vfzBaZ2RNmptNDSSTMjHEDOvDarafzo3F9mLF8M2PvfZOfPFvMhu174l1eUphUHMY83RXzpJJY7PF/F/i41vU7gXvcvSewGfh6DGqQNNYoK5NrR/Rg2u2juHJ4Fx6fvpJRd03lwamL2V1RFe/yElYwN09wQvUsxTwpJdK/ppl1AsYDfwmvGzAaeCpcZSJwQZQ1iNTIb5rDL87vz8s3j+CEbvnc+dJ8xvx2Gv+duwZ3j3d5CWfqglJ2ajRPSor6bfz3wPeB6vB6a6DM3SvD66uAo+ra0MyuNbMZZjajtFRfzEnD6dm2GQ9ffTyPfmM4zRtnc9Pjs7nwwXeYuXxzvEtLKIWKeVJWZI3fzM4F1rv7zM+zvbtPcPdh7j6soKCggasTgVN6tuGFm07lN18ayKrNu/jSg+9w42OzWLlpZ7xLi7ua0TyKeVJTlOP4TwHOM7NxQC7QHLgXaGlmWeFefydgdYQ1iBxUZoZxyfGdGT+wAw+9sYQJbyzmlY/W8bVTunH9qB40z82Od4lxMXXBenaWVzF+gM60lYoieyt39zvcvZO7dwUuBV539yuAKcBF4WpXAc9FVYNIfTVtlMWtZx7DlNtGcu7ADvxp2mJG3jWVf7y3nMqq6kPfQYopLF5LftMcTuyef+iVJenE4zPcD4BbzWwRQeb/cBxqEKlThxaN+d0lg/nvjafSq20zfvrsPMbe+yZT5q9Pmy+Aax+0pZgnNcXkr+ruU9393PD3Je5+grv3dPeL3V0DqiXhDOjUgn9deyIPfeU4KququeZvH/DVv05n/tqt8S4tcp/GPBrNk6r0di5yAGbG2f3a88otp/Ozc4+laNUWxt37Jnc8XcT6bbvjXV5kXigqUcyT4tT4RQ4hJyuDr53ajWm3j+Tqk7vx5IxVjLprKve9vjDlDgDbVV7F6/PXK+ZJcfrLitRTyyY5/OwLx/Lqradzaq823P3KJ4y+eyrPzF5FdXVq5P81Mc+5mpsnpanxixymbm2a8tBXhvGva08kv1kOtzwxlwseeJvpSzfFu7QjVlgcxDzDuynmSWVq/CKf04ndW/P8Dafyu0sGsX7rHi556F2+/c+ZLN+4I96lfS67yquY/PF6HbSVBnQiFpEjkJFhXDi0E+f078Cf31zCn6Yt5rWP13HVSV25aXQvWjRJngPApi5Yz64KjeZJB3pbF2kAjXMy+c6YXky9bSQXDunEw28v5fS7p/DI20upSJIDwF4oLqG1Yp60oMYv0oDaNs/lzosGUnjTafTr2Jxf/Pcjzr7nDV79aF1CHwC2q7yK1z9ez9mKedKC/sIiETi2Y3P++fXh/PXqYZjBN/8+g8v//D7zVm+Jd2l1mhLGPOcq5kkLavwiETEzRvdpx0s3j+B/z+/H/LVb+cJ9b3Hbk3NZuyWxDgArDGOeExTzpAU1fpGIZWdm8NWTujL19lFce1p3np+zhlF3T+WeVz9hZ3nloe8gYjUxj0bzpA/9lUVipEXjbO4Y15fXbj2d0X3acu/khYy6eypPzlgZ1wPApmg0T9pR4xeJsS6tm3D/FUN56rqTaN+iMbc/VcQX7nuLdxZviEs9hUUltGmmmCedqPGLxMmwrvk88+2TuffSwZTtrODyP7/PNybOYHHp9pjVsLO8UnPzpCH9pUXiKCPDOH/wUUz+3ul8f2xv3luykbPveYOfP/8hm3eUR/74U+aXBjGP5uZJK2r8IgkgNzuT60f2ZMptI7nk+M78/d1lnH7XFP7y5hL2VEY3A+ik4iDmGd5NJ1RPJ2r8IgmkIK8R/++LA3jxuyMY0qUVvyz8mLPueYMXi2rOCQ8AAAntSURBVEsa/ACwneWVTJ4fnFA9M8Ma9L4lsanxiySg3u3zmPi1E/jbNcfTKCuDbz86i0seepe5K8sa7DGmzC9ld0U14zSaJ+2o8YsksJG92zLpO6fx/744gKUbdnD+/W9zyxNzWFO264jvu7B4jWKeNKXGL5LgsjIzuHx4F6bcNpLrR/agsLiEUXdP5e6XF7B9z+c7AKxmNI9invSkxi+SJPJys/n+2D68/r3TGdu/PfdNWcTIu6by+PQVVB3mAWCvz1/P7opqxg/oGFG1ksjU+EWSTKdWTbj30iE8c/3JHN26CXc8Xcz4P7zJmwtL630fwWieRjpoK02p8YskqSFdWvHUdSfxwBVD2VFeyVcens41j0xn4bptB92uJuY5RzFP2lLjF0liZsa4AR147dbT+dG4PsxYvpmx977JT54tZsP2PXVuUxPzaDRP+lLjF0kBjbIyuXZED6bdPoorh3fh8ekrGXXXVB6cupjdFfseABbMzaOYJ51F1vjNLNfMppvZXDP70Mx+ES7vZmbvm9kiM3vCzHKiqkEk3eQ3zeEX5/fn5ZtHcEK3fO58aT5jfjuN/85dg7uzY08lUxYo5kl3Ue7x7wFGu/sgYDAw1sxOBO4E7nH3nsBm4OsR1iCSlnq2bcbDVx/Po98YTvPG2dz0+GwufPAd7p+yKBjNo7l50lpkjd8DNdMMZoc/DowGngqXTwQuiKoGkXR3Ss82vHDTqfzmSwNZtXkXD0xdTJtmjTi+q2KedJYV5Z2bWSYwE+gJ3A8sBsrcveaok1XAUQfY9lrgWoAuXbpEWaZISsvMMC45vjPjB3Zg4rvL6Nq6qWKeNBdp43f3KmCwmbUEngH6HMa2E4AJAMOGDYvf6YlEUkTTRllcP7JnvMuQBBCTUT3uXgZMAU4CWppZzRtOJ2B1LGoQEZFAlKN6CsI9fcysMXAm8DHBG8BF4WpXAc9FVYOIiHxWlFFPB2BimPNnAP929xfM7CPgX2b2S2A28HCENYiIyH4ia/zuXgQMqWP5EuCEqB5XREQOTkfuioikGTV+EZE0o8YvIpJm1PhFRNKMuSf+sVFmVgosj3cd9dAG2BDvIg5TstWcbPWCao6VZKs5FvUe7e4F+y9MisafLMxshrsPi3cdhyPZak62ekE1x0qy1RzPehX1iIikGTV+EZE0o8bfsCbEu4DPIdlqTrZ6QTXHSrLVHLd6lfGLiKQZ7fGLiKQZNX4RkTSjxn+YzKyzmU0xs4/Ck8h/t451RprZFjObE/78LB617lfTMjMrDuuZUcftZmZ/MLNFZlZkZkPjUWdYS+9az90cM9tqZjfvt07cn2Mz+6uZrTezebWW5ZvZq2a2MLxsdYBtrwrXWWhmV8W55rvMbH74d3+mZjr1OrY96GsoxjX/3MxW1/r7jzvAtmPNbEH4uv5hHOt9olaty8xszgG2jc1z7O76OYwfgummh4a/5wGfAMfut85I4IV417pfTcuANge5fRzwImDAicD78a45rCsTWEtwIEpCPcfACGAoMK/Wst8APwx//yFwZx3b5QNLwstW4e+t4ljzWUBW+PudddVcn9dQjGv+OXBbPV47i4HuQA4wd///q7Gqd7/bfwv8LJ7Psfb4D5O7l7j7rPD3bQQnl6nzvMFJ5nzg7x54j+BMaR3iXRQwBljs7gl35La7vwFs2m/x+cDE8PeJwAV1bHo28Kq7b3L3zcCrwNjICq2lrprd/RX/9DzY7xGcGS9hHOB5ro8TgEXuvsTdy4F/Efx9InWwes3MgEuAx6Ou42DU+I+AmXUlOOfA+3XcfJKZzTWzF82sX0wLq5sDr5jZzPBE9vs7ClhZ6/oqEuMN7VIO/J8k0Z5jgHbuXhL+vhZoV8c6ifpcA3yN4JNfXQ71Goq1G8N46q8HiNQS8Xk+DVjn7gsPcHtMnmM1/s/JzJoB/wFudvet+908iyCaGAT8EXg21vXV4VR3HwqcA9xgZiPiXdChmFkOcB7wZB03J+JzvA8PPrsnzXhpM/sxUAk8eoBVEuk19CDQAxgMlBDEJ8ngMg6+tx+T51iN/3Mws2yCpv+ouz+9/+3uvtXdt4e/TwKyzaxNjMvcv6bV4eV64Bk+exa01UDnWtc7hcvi6Rxglruv2/+GRHyOQ+tqIrLwcn0d6yTcc21mVwPnAleEb1ifUY/XUMy4+zp3r3L3auDPB6gloZ5nM8sCLgSeONA6sXqO1fgPU5jRPQx87O6/O8A67cP1MLMTCJ7njbGr8jP1NDWzvJrfCb7Mm7ffas8DXw1H95wIbKkVWcTLAfeOEu05ruV5oGaUzlXAc3Ws8zJwlpm1CiOKs8JlcWFmY4HvA+e5+84DrFOf11DM7Pf90xcPUMsHQC8z6xZ+eryU4O8TL2cA8919VV03xvQ5jvrb41T7AU4l+PheBMwJf8YB1wHXhevcCHxIMIrgPeDkONfcPaxlbljXj8PltWs24H6CURDFwLA419yUoJG3qLUsoZ5jgjelEqCCID/+OtAamAwsBF4D8sN1hwF/qbXt14BF4c81ca55EUEWXvN6/lO4bkdg0sFeQ3Gs+R/h67SIoJl32L/m8Po4gpF3i2NVc131hsv/VvP6rbVuXJ5jTdkgIpJmFPWIiKQZNX4RkTSjxi8ikmbU+EVE0owav4hImlHjl7RhwcyqS80sP7zeKrze9TDuY3uE9Z0XqxkkJb1pOKekFTP7PtDT3a81s4eAZe7+q8PYfru7N4uuQpHoaY9f0s09wIkWzO9/KnB3XSuZ2ZVmNj2cF/0hM8vc7/Y2ZvaumY03sw5m9ka47jwzOy1c56xwnVlm9mQ4v1PNnOu/CJcXm1mfcPnVZnZfpP96EdT4Jc24ewVwO8EbwM3h9X2YWV/gy8Ap7j4YqAKuqHV7O6CQYE71QuBy4OVw3UHAnHDeoJ8AZ3gw6dYM4NZaD7MhXP4gcFvD/0tFDiwr3gWIxME5BIfU9yeYC39/Y4DjgA/C6YAa8+lka9kEUzLc4O7TwmUfAH8NJ+971t3nmNnpwLHA2+F95ADv1nqMmsn9ZhJM3CUSM2r8klbMbDBwJsFZxt4ys3/5ZyejM2Ciu99Rx11UEjTrs4FpEJx4I5w+dzzwNzP7HbCZ4GQrlx2glD3hZRX6fygxpqhH0kY4m+eDBBHPCuAu6s74JwMXmVnbcLt8Mzs6vM0JJljrY2Y/CG8/muDkGn8G/kJw2r33gFPMrGe4TlMzOya6f51I/WlPQ9LJN4EV7l4T7zwAXGNmp9eKbXD3j8zsJwRnQsogmGXxBmB5eHuVmV0GPG9m24AdwO1mVgFsB77q7qXhHPePm1mj8K5/QjBTpEhcaTiniEiaUdQjIpJm1PhFRNKMGr+ISJpR4xcRSTNq/CIiaUaNX0Qkzajxi4ikmf8PsQfXI/CGnOcAAAAASUVORK5CYII=\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 297
        },
        "id": "-Sb8fQqdi5Dp",
        "outputId": "5ea90a68-12f6-4b40-b27b-9991aca40a85"
      },
      "source": [
        "plt.plot(x,y,'r*--')\n",
        "plt.xlabel(\"X ekseni\")\n",
        "plt.ylabel(\"Y ekseni\")"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Text(0, 0.5, 'Y ekseni')"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 128
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 283
        },
        "id": "CNTElYHri45N",
        "outputId": "968891b6-3240-4a41-d574-bf24b27eb96b"
      },
      "source": [
        "plt.plot(x, \"go-\")\n",
        "plt.plot(y, \"b--\")"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[<matplotlib.lines.Line2D at 0x7f453392bf90>]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 130
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 617
        },
        "id": "eg6FZfIPi42F",
        "outputId": "c587bdd6-0678-4b40-926c-935889225a73"
      },
      "source": [
        "data=pd.read_csv(\"https://raw.githubusercontent.com/parmarjay/datafiles/master/AAPL.csv\",index_col=0 , parse_dates=True)\n",
        "data"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
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
              "      <th>Open</th>\n",
              "      <th>High</th>\n",
              "      <th>Low</th>\n",
              "      <th>Close</th>\n",
              "      <th>Volume</th>\n",
              "      <th>ExDividend</th>\n",
              "      <th>SplitRatio</th>\n",
              "      <th>AdjOpen</th>\n",
              "      <th>AdjHigh</th>\n",
              "      <th>AdjLow</th>\n",
              "      <th>AdjClose</th>\n",
              "      <th>AdjVolume</th>\n",
              "      <th>Name</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Date</th>\n",
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
              "      <th>2018-03-27</th>\n",
              "      <td>173.68</td>\n",
              "      <td>175.15</td>\n",
              "      <td>166.9200</td>\n",
              "      <td>168.340</td>\n",
              "      <td>38962839.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>173.680000</td>\n",
              "      <td>175.150000</td>\n",
              "      <td>166.920000</td>\n",
              "      <td>168.340000</td>\n",
              "      <td>38962839.0</td>\n",
              "      <td>AAPL</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2018-03-26</th>\n",
              "      <td>168.07</td>\n",
              "      <td>173.10</td>\n",
              "      <td>166.4400</td>\n",
              "      <td>172.770</td>\n",
              "      <td>36272617.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>168.070000</td>\n",
              "      <td>173.100000</td>\n",
              "      <td>166.440000</td>\n",
              "      <td>172.770000</td>\n",
              "      <td>36272617.0</td>\n",
              "      <td>AAPL</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2018-03-23</th>\n",
              "      <td>168.39</td>\n",
              "      <td>169.92</td>\n",
              "      <td>164.9400</td>\n",
              "      <td>164.940</td>\n",
              "      <td>40248954.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>168.390000</td>\n",
              "      <td>169.920000</td>\n",
              "      <td>164.940000</td>\n",
              "      <td>164.940000</td>\n",
              "      <td>40248954.0</td>\n",
              "      <td>AAPL</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2018-03-22</th>\n",
              "      <td>170.00</td>\n",
              "      <td>172.68</td>\n",
              "      <td>168.6000</td>\n",
              "      <td>168.845</td>\n",
              "      <td>41051076.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>170.000000</td>\n",
              "      <td>172.680000</td>\n",
              "      <td>168.600000</td>\n",
              "      <td>168.845000</td>\n",
              "      <td>41051076.0</td>\n",
              "      <td>AAPL</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2018-03-21</th>\n",
              "      <td>175.04</td>\n",
              "      <td>175.09</td>\n",
              "      <td>171.2600</td>\n",
              "      <td>171.270</td>\n",
              "      <td>35247358.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>175.040000</td>\n",
              "      <td>175.090000</td>\n",
              "      <td>171.260000</td>\n",
              "      <td>171.270000</td>\n",
              "      <td>35247358.0</td>\n",
              "      <td>AAPL</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2013-12-26</th>\n",
              "      <td>568.10</td>\n",
              "      <td>569.50</td>\n",
              "      <td>563.3760</td>\n",
              "      <td>563.900</td>\n",
              "      <td>7286000.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>75.513273</td>\n",
              "      <td>75.699365</td>\n",
              "      <td>74.885347</td>\n",
              "      <td>74.954999</td>\n",
              "      <td>51002000.0</td>\n",
              "      <td>AAPL</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2013-12-24</th>\n",
              "      <td>569.89</td>\n",
              "      <td>571.88</td>\n",
              "      <td>566.0300</td>\n",
              "      <td>567.670</td>\n",
              "      <td>5984100.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>75.751204</td>\n",
              "      <td>76.015720</td>\n",
              "      <td>75.238124</td>\n",
              "      <td>75.456116</td>\n",
              "      <td>41888700.0</td>\n",
              "      <td>AAPL</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2013-12-23</th>\n",
              "      <td>568.00</td>\n",
              "      <td>570.72</td>\n",
              "      <td>562.7600</td>\n",
              "      <td>570.090</td>\n",
              "      <td>17903800.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>75.499981</td>\n",
              "      <td>75.861530</td>\n",
              "      <td>74.803467</td>\n",
              "      <td>75.777789</td>\n",
              "      <td>125326600.0</td>\n",
              "      <td>AAPL</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2013-12-20</th>\n",
              "      <td>545.43</td>\n",
              "      <td>551.61</td>\n",
              "      <td>544.8175</td>\n",
              "      <td>549.020</td>\n",
              "      <td>15586200.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>72.499920</td>\n",
              "      <td>73.321381</td>\n",
              "      <td>72.418505</td>\n",
              "      <td>72.977112</td>\n",
              "      <td>109103400.0</td>\n",
              "      <td>AAPL</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2013-12-19</th>\n",
              "      <td>549.50</td>\n",
              "      <td>550.00</td>\n",
              "      <td>543.7301</td>\n",
              "      <td>544.460</td>\n",
              "      <td>11439600.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>73.040915</td>\n",
              "      <td>73.107376</td>\n",
              "      <td>72.273965</td>\n",
              "      <td>72.370985</td>\n",
              "      <td>80077200.0</td>\n",
              "      <td>AAPL</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>1072 rows × 13 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "              Open    High       Low  ...    AdjClose    AdjVolume  Name\n",
              "Date                                  ...                               \n",
              "2018-03-27  173.68  175.15  166.9200  ...  168.340000   38962839.0  AAPL\n",
              "2018-03-26  168.07  173.10  166.4400  ...  172.770000   36272617.0  AAPL\n",
              "2018-03-23  168.39  169.92  164.9400  ...  164.940000   40248954.0  AAPL\n",
              "2018-03-22  170.00  172.68  168.6000  ...  168.845000   41051076.0  AAPL\n",
              "2018-03-21  175.04  175.09  171.2600  ...  171.270000   35247358.0  AAPL\n",
              "...            ...     ...       ...  ...         ...          ...   ...\n",
              "2013-12-26  568.10  569.50  563.3760  ...   74.954999   51002000.0  AAPL\n",
              "2013-12-24  569.89  571.88  566.0300  ...   75.456116   41888700.0  AAPL\n",
              "2013-12-23  568.00  570.72  562.7600  ...   75.777789  125326600.0  AAPL\n",
              "2013-12-20  545.43  551.61  544.8175  ...   72.977112  109103400.0  AAPL\n",
              "2013-12-19  549.50  550.00  543.7301  ...   72.370985   80077200.0  AAPL\n",
              "\n",
              "[1072 rows x 13 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 136
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 306
        },
        "id": "ecojgLn3qWPK",
        "outputId": "14de8de4-c2ee-495a-bb5b-ed7e3633fc0c"
      },
      "source": [
        "data.Volume.iloc[:100].plot()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7f4533878210>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 138
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 303
        },
        "id": "oieikyeerRcr",
        "outputId": "b448831a-0f68-4cab-d88a-eb4036cf62b0"
      },
      "source": [
        "data[['AdjOpen','AdjClose']][:50].plot()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7f4534447e50>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 139
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYkAAAEMCAYAAAAxoErWAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAgAElEQVR4nOydd3zU9f3Hn5+7y96b7AUh7BECyJLhRC2Ku1q3uGq1y9bRWtvaWmt/tnXUrdUqDtytIgrIXmGvAFkkFyB77+Q+vz8+l0suAwIkl0vyeT4eeVzy+Xzue5/A5V7fz3sKKSUajUaj0XSFob83oNFoNBrnRYuERqPRaLpFi4RGo9FoukWLhEaj0Wi6RYuERqPRaLrF1N8b6E2Cg4NlXFxcf29Do9FoBhTbt28vllKGdDU3qEQiLi6OtLS0/t6GRqPRDCiEEEe7m9PmJo1Go9F0ixYJjUaj0XSLFgmNRqPRdIsWCY1Go9F0ixYJjUaj0XSLFgmNRqPRdIsWCY1GM6jIKa5h7eGi/t7GoEGLhEajGVT88X8HuePtNGoamvt7K4MCLRIajWbQUN/UwoaMYhqbLWzIKO7v7QwKtEhoNJpBw6asEuqaWgBYebCwn3czOBhUZTk0Gs3QZnV6IR4uRmYOD2bVoUIsFonBIPp7WwMafZLQaDSDAiklq9ILmTk8mIXjhlFU1cDe/Ir+3taAR4uERqMZuJTnwr8vg13vcaSwGnNZHfOTQ5k7MhSDgJXp2uR0tmiR0Gg0AxPzdnh1AWSvhe+fYtXBEwDMTw4l0MuVyTEBrDxY0M+bHPhokdBoNAOPA5/DW5eAizuc+ysoP0rB7u8YHe7LMD93ABaMCmP/sUpOVNT382YHNlokNBrNwEFK2PAP+PAmGDYW7lgFs36Kxc2PicVfsmBUqG1p6/cr0/Vp4mzQIqHRaAYGLU3w5QPw7W9hzGK4+UvwDgEXD3IiLuEiw1bOi3ezLR8R6k10oAerdCjsWaFFQqPROD915fDuVbDj3zD753Dl6+DiYZv+WM7DTTQxrnSFbUwIwYLkMNZnFFPX2NIfux4UaJHQaDTOTVkOvHEh5KyHRS/Agt+Coe2jq8UieTfXH7P7CAw737F76oJRoTQ0W9iYqbOvzxQtEhqNxnkxp8Fr50HVcfjRpzDpxk5LduaWUV7bRNnI6+DEHji2yzY3NT4QL1ejDoU9C7RIaDQa52T/ZyqCydUL7lgJ8XO6XLYqvRCTQRAz9xYwuUO704SbycicpBBWHSxESumgjQ8uHCoSQog3hBCFQoh97cYmCiE2CyF2CSHShBBTreNCCPFPIUSGEGKPEGKyI/eq0Wj6CSlh3f/BRzdD+AQlEMEjulza1GLhm/0nmBIXgF9AMIz6Aez5CJrqbGvmJ4dyorKeffmVjvoNBhWOPkm8BVzUYexp4Akp5UTgt9afAS4GRli/lgD/ctAeNRpNf9HcCF/8GFY+AWOvgpu+AK/gLpdKKXns031kFtVww7RYNTj5R9BQAQe/tK07f3QYrkYDn+7Md8RvMOhwqEhIKdcCpR2HAV/r937AMev3i4C3pWIz4C+ECHfMTjUajcOREj64EXb+RyXIXfmaSpbrhhdWZ/BBWh73zx/OZRMi1GDsLAiIgx1v29b5e7qyYFQon+/Kp6nF0se/xODDGXwSDwJ/FULkAc8AD1vHI4G8duvM1jE7hBBLrGaqtKIi3Y1KoxmwVJjhyDdKIOY9AqL76q2f7jTzzIrDLJ4Uyc/OT2qbMBgg5RbIWQcFB2zDV6VEUVLTyPeH9GfE6eIMInEP8FMpZTTwU+D103mylPIVKeUUKeWUkJCQPtmgRqNxAOat6jGpo0Xano2ZxTy0bA/nJATx1JXjER3FZPLN4OIJm1+wDc1JCiHY25WPt5t7e9eDHmcQiZuBT6zffwRMtX6fD0S3WxdlHdNoNIORvG1g8oBh47pdcrigirve2U5ckBcv/SgFV1MXH2GegTDxh8qBXa1CX12MBhZNjGRlegFlNY199RsMSpxBJI4B51q/nw8csX7/BXCTNcppOlAhpTzeHxsE2JdXyl2vfsex8rpTL9ZonBin7f1s3goRk8Do0uV0YWU9t765DXcXI2/emoqfR9frAJh2D7Q0wLY2w8RVKVE0tUi+2H2s++dpOuHQznRCiKXAXCBYCGEGHgfuBP4hhDAB9ahIJoCvgIVABlAL3OrIvdLcCPlpcHQj5G5iRPYmnmuu57FXHufRH9+Ln+dJ3qAajZMgpeRQQRXbskvZllNGWk4pxyrqWTIngYcvTu5squkvmurh+B44594up2samrnt39soq23kw7vOISrA8+TXCx6uzFbbXoNZPwUXd0aF+zI63Jdl283cPCOu93+HQYpDRUJKeX03UyldrJXAfX27o5Ow7FZI/6/6PmQU693PJa5mL4/VPMXjbwzjz3ddhbuLsd+2p9F0SVWBuhP3DATg3S25PPaZSksK83UjNS6QSRJeWZuFl6uJB87rOv/A4RzfBZYmiJ7Waaq5xcKP39vBweNVvHbTFMZG+vXsmufcpxoS7f0QJt8EwJUpUfzhvwc4XFBFUphPb/4GgxZnMDc5H5YWyFoDY66Ah7Kx3LOJB6tv4dPRz+Lm7sGDhY/xm6VraLHoDE6NE9FQBa/MhRemqYY8qJ7P0YEerP3lPDY/vIDnfziZ566fxFUpUTz73WFeX5/dv3tuJc/qtI6aajcspeS3X+xn9aEi/rBoLPOSQ7t4cjfEzYawcbDpRRVeCyyaGIHJILQD+zTQItEVBfuhsQpGXgKegWQV11DV0ExsQjJuN35ApKmcqzN+zZ++2KVT/TXOw5q/QNUxdZJ46xJa9n/G1pxSZiYGExPkaTMtGQyCpxaP4+Kxw/jDfw/w4ba8U1zYAZi3qvwGb/sIxZfWZPHellzumZvID6fFnN41hVCniaKDkLkKgGBvN+aODGX9jj00N7Y1IyqubqCgUjcn6gotEl2Ru1k9xqij7+68cgAmRvtDdCqmxS8x1XCIMdsf49fL9lBZ39RfO9VoFEWHYPO/YNKP4K61MGwcxo9u5odNnzI9PrDTcpPRwN+vm8jsEcH8+pM9LN93oh82bUVKFdnU4RTx+a58/rI8nR9MiOCXF4w8s2uPvRK8w2DTC+o1vvsdfy9ewv+al1Dyf+fw2/98x5ynVzPlj98x86lVPPPNIRqadVnx9miR6IrcTeAbCX4qAne3uRxvNxMJId5qfuyVWOY+wmLjelL3PMZlf/uGFfv78Y9MM7SREr76pSqEd97vVBmLm78kK+xCHnZZygVHfgelnc1KbiYjL/8ohfhgL15bl+XoXbdRkQfVJyC6TSS2ZJXwy4/2MDU+kL9ePR6D4Qwd7CZXmHonZK6E18+DDf/EMyiSV8TVeNUd466Me5gTXMUjC5O5fFIkz6/O4JJ/rmdHblkv/XIDH4c6rgcEUqqTRMx0W8bn7rxyxkX6YWz3RjWc+xBYmrhy7TNMb8nk7v/cw2djZ/C7H4wh1Kf7UgIaTa9z4HPIXgMLn2mrc+Tizl88f8EMky83p38MBz+ChHkqG3nkQvXhCXi6mpgYHcCm/uy3YPNHpAKQUVjNkne2Ex3owSs/SsHNdJYBIlOXqKZFw8bDiPMxeAbyg4p6ao7dSsQXN/DH0l/AyE9hzgQumxDBwx/v4cp/beS2mfH84oKReLgO7QAVfZLoSEWesuvGnANAQ3MLB45XMiHa336dEDD/McTNXxLpLfnc/XfEpr/OBX/7ng/T8rSvQuMYGmvgm0eVgzalLUrcYpFsOVrOvpH3w4P7YN6jUJKhKqs+O9quZEVkgAcnKuv7r66ReZvKkA4bS1FVA7e8uRUXo+CtW6fi7+l69td394MLn4QJ19qivob5uRM2aibi1uUgjPDmxZC3lXOTQljxs3O5cVosr6/P5sK/rx3yDYu0SAC1jc28tyWXoyU1kLtFDcZMB+Dg8SqaWiQTo7sJu4ufjbh7A8bki/mV8V3edv0zzyxbw49e30puSa2DfgPNkGXd36DSDJc8A8Y2w8ChgirKa5uYlhAEfpFw7kPwwG744UdQVwZ7P7KtjfR3xyLpdcfttwcKKK5uOPXCvK0QMRlpMHLXO2mUVDfyxi2pRAeeIheiNwhNhtuWg2cQvLMYSjLxdjPxh8vH8v6S6RgE/PDVLTzy6V6qhqjvUYsEUN3QzG8+38d7W3OVP8LVB8LGAG1O6/FR/t1fwDMQrnkHLvsn4+Rh1vo8in/ed1z497W8ti5Lh8pq+oaSTNj4HIy/znZT08qWrBIAprV3WhuMkHSBKnth3mYbjvBXvaKPlfeeSByvqOPOt9N4de0pfB1NdaqbXHQqmUXV7Mgt56GLRp787623CYhVJckNRvjoFpXYB0xPCOLrB+Zw5+x43t+aywXPrmX1EOxwp0UCCPVxZ97IUD7eno/M3QTRqeoNg3Jah/i4Ee53Cj+DEJByM2LJGtyDYnhePM0L/u/y1//tZvGLGzh4XDc80fQiUsLXD4HRDc7/fafpLdmlRPp7dH03HpUKx3aqfCDai0TvlZzZbBWptKOncAAf2wWWZoiaytrDyqxz3qiwXttHj/GPhiteUoK14jHbsIerkUcvGc3H98zA283ErW9t42cf7BpS9Z+0SFi5NjWaxupSKDwI0W13ZbvzypkQ5d/z8gUhSXDHd3DOj5lf9QVpIX/AvfQglz23nr+t0OF1ml7i0FeQ8R3Mexh87D9UpZRszS61P0W0J3IKNFZDUToAEX5KJPJ7UyQyVduYveaKk7/n86zm3ahU1h0pIiHYyzFmpq4YeTGc82PY9qpqndqOSTEB/Pcns/jJ/OF8sfsY5z+7hq/29lspOYeio5uszBsZwjyvHESLtB3dK+ubyCyq4YpJndpYnByTm3KUDV+Az6d38754lM+il/DTVRa+2nucc5Pss0ZdTIIAT1cCPF3w93Ql0t+j56UHNEOPpjpY/msIGaUidzqQUVhNSU0j0xK6EYmoKerRvA3CxuDhaiTIy7V3RSK7BB83E1UNzezLryAltpu9mLdBQDwN7oFsztrONVOiem0PZ8R5v1PRjV/cD+HjITDBNuVmMvKzC0Zy0dhwfrlsN/e+u4PFkyL52zUTnKcGVh+gRcKKyWjg2mHHaDYbKPEbSxjqLgjoHNnUUxLnwz0bEZ/fxxWHn2NO/B7uqrqdj9LsnXkNzRYaO0SWfH7fzDN/Xc3gZv3foTwXbv5vlxVTN2eru/jpCUFdPz8wATwCwZymQmJRJqfeMjcdK6/jaEkt985N5MXvM9l+tKxrkZBSOa0T57P9aBl1TS3MHtHPPWGMLnD1m/DSLOWfuP1bddPXjtERvnx230ye/N9B3tqYw51zEhgV7tv19QYB2tzUjkkynf0yjmV7lB11V6vTOvIsPqy9guH692HhMwQVbWGZ/Dl7R73N3vjn2BvxJHsDf8Wh1C/Z/8SFbPj1fD66W4Xers8Y2mF3mm4ozYb1z6pM4vjZXS7ZklXCMF93Yroz2wihThPmNNtQhL87+WW9IxKt/ohLx0cQG+RJWk43fonyo1BTCNGprDtSjMkgmJ7YjbA5Ev8YuPxfcHw3rPhNl0tcjAbumzccg4Cv+zNb3QFokWiluRGPwp2YfSbwkTXPYXdeOQnBXmdfFlwIlfV552oIHqn+0C3N4D0M3LwRu9/Hi3oi/T1IjQtkRKg3W7I7tgLXaIBvHgGDCc7/Q5fTUkq2ZJcyLSHw5CaQqFTlk6hXARWtJ4kzyu9paYLstbD5Jchex44jefh7upA8zIeU2AB25JZ1fd3sdeoxehrrjhQxOTYAbzcnMW4kXwLT74OtL6tkxS4I8VFVdZfvG9y+CSf5H3ECTuyB5noCJ8whZ0MtW7JL2W0uZ0ZicO+9RthouPV/9mMZK+E/i1WBs8T5AExLCOTTHfk0t1gwGbWOa6wcXqEc1uc9oXIfuiC7uIaiqgamxZ/ijjwyBZBwbAckzCXS34OaxhYq65p7dlNUW6oc54e+Vu/hhgrb1BMYWOKagOGr5cwM+yGf7GjkaEktccFe9tfY+xEExFPiNYJ9+Sv5xQVJOBXn/Q7yNsPn96ts7cD4TksWjgvn8S/2k1FYzfBQb4dv0RHoT6BWcjcBMHHmRfi4mfjnyiMUVDYwIaqPHcjRU0EYVHMjK9MTgqhpbGHfMR02q7HS3ADLfwVBI2B61415ANsJtFundSuR1hYu1nyJSP9TRDhJCUWHYcM/4c2F8Nfh8MmdkLMeRl8G174LPztI8aJ3eb55EUbvYNj5DufnPQfA9o6hsJXH1elj/DWsz1TmqX73R3TE5ApXvaG+X3abakTWgQvHDAMY1KcJLRKt5G6GgHg8AiO4bGIEG61v3D53Hrv5QPgEO5GYag1dbE2I0mjY+ByUZsHFf7HVXeqKLVklBHu7kdDxrr0jHv4QnGTzS0R0JRKtZqTlj8Bzk+GFVPj2N8pENftncMcq+PkhWPQCjLoUfCNYY5nIs81XU3n1RzDlNnyy/kese03nfIn9nwASxl3DuiPF+Hm4OGdEX0AcXP6COnF9+9tO08P83Jkc489XewevX0KLBNgX9QOuS1XVX12MwjFRC7Ez1R9rs4p6CvVxJyHEy+YA1AxxyvNg7TMw6jIYvqDbZXvNFXy19wTzRob0LCQzKlW976S0T6irMMOy2+HpRNXZbdtrEJioCgg+uA/uWQ/zH4OoFDDYf4RsziohwNOFkWE+MOV2hKWJH/ttYkdHkdjzIURMQgYlsu5IEbOGB9sV0HQqRl0G0+6GLf+Cg//tNL1wXDgHjleqsj6DEC0SoIr61ZXaRGJcpB+jw30ZG+nnmBalMeeopu35O2xD0+KDSMsp0yU9NLDiUfV44Z+6XVJR18S9720n2NuVRxaO6tl1o6ZAbTGU5RDk5YqryaBE4ssHle+j1Yz0UBbcuEwFX/hHn/SSm7JKmBYfpEp7hyRB/BwurP+KjMIKKuqstY+Kj6h2peOu4UhhNQWVDcwe0Yu+v77g/N9DxCT4/F4oO2o31WpyGqxRTlokQIW8/eqoCisEhBC8eWsqL94w2TGvb604S257v0QgVQ3NHNB+iaFN5moVXTP75+p92gVSSn750W6Ol9fz/A2TCfDqYeXUyNakujQMBkGkvwc++Wsh41uY90ibGcmtZw7ZvNJazGV1TG/vD0m9A9+GE8wVO9nZ2qNhz4fKDzd2MWsPFwEwy9lFwuQGV72prA7LbrXzT0QHejI+yk+LxKDH3Vf5B6yE+boTbi1X0Od4BUFIsp1fojU6ZUu2NjkNWZobVX2mgHiYcX+3y15fn82KAwU8vHAUk2MCen790NGqRHe+8ktE+rlw6YkXlR2+i0zuU9HqNLfLdRi5EIv3MH5k+k45r6WEvR9C/BzwGca6I8UkhHgRFdBPpThOh8B4WPQ85G+H735nN3XR2GHszivv1ax1Z0GLhLMQO0OVKbcWXRvm505ckCebs3S+xJBly0tQfFg5q126LjC5/WgpT32dzoVjwrhtZtzpXd9oUiYUa4TTIvk9cS05KsS2Q5ZxT9icVUKglytJoW03WxhdMKTcwhzDHvIy9ysfSFkOjLuGhuYWtmSXMMfZoppOxuhFSkA3vwDpX9mGLx4bDtC/bWD7CC0SzkLMDGisghN7bUPT4oPYml2i/RJDESlVX+bE+ZB0YZdLSmsa+fF7O4nw9+Dpq86wflDUFDi+B2pKWFj0GtssSTQmXXZGW96UWcK0+MDOrUZTbkZiYNyJT7Ds+QBM7jDqMt7fmkd9k8X5/REdueCPKiLxs3tUeRQgPtiL5GE+fD0Ii/45TCSEEG8IIQqFEPvajX0ghNhl/coRQuyyjscJIerazb3kqH32G7GtfolNtqFpCYFU1jeTfkL7JYYcZTmq73PyJV1OWyySBz/YRUlNIy/eMBk/jzOsChCVCpYm+OQOvJpKebLpRgqqetAoqAN5pbXkl9d1XS/KN4KCiAUsZjWWvZ9gGXERv1uRx+Nf7GdGYpDz+yM6YnKDq98CaYG3F8Gnd8OK3/CI/0qGmb8i49jgKqnjyIzrt4DngbdbB6SU17Z+L4T4G1DRbn2mlHKiw3bX3/hFKcfk0Q0w/R4A1VUM2JJVypgIJ4wh1/QdrSW0o6d3Of3i9xmsPVzEk1eMPbv8glbndeYqiuIuY1f6cMxldaddrvvtTTkAzOim9pLLOUsI+HgF1Ffz9IkJvHU8hztmxfPri5MHZlWBwATlyP7+TyqhsLqQOS0NzHGBB59vIT30YuYlh7IgOZRJMQHOG97bAxz2vyOlXAt0aWAX6px8DbDUUftxSmJnwtFNytQA1qYxHtp5PRTJ3QxuvhDaOZx1Y2Yx//ftYRZNjOCHU7uOeOoxvuHgGwVGN+rnqGJ2p1sN9qO0PF5dl80Pp8UwIsynyzXBYxaQQyTl0ot3ikfwj+sm8tilowemQLQy4jy4cxX8dB88VgC/ykEa3bh1eDX+ni68ujaLq17axKOf7j31tZwYZ6ndNBsokFIeaTcWL4TYCVQCj0kp13X1RCHEEmAJQEzMWf7B9Dcx58DupSqOPETVsZkWH8TKgwVYLLKzrVczeMnbokxBBvs8ncLKen6ydBfxwV786YpxvdPHYP6jgCAkejiQcVoisSWrhEc+3cus4cE88YMx3a4TBgNfj/wjh46aef+mOYPvZCwEeAQgQpKY4HqM9287h8r6Jm5/axt7zBWnfr4T4ywicT32p4jjQIyUskQIkQJ8JoQYI6XsZJyXUr4CvAIwZcqUge3hjZ2pHnM3thOJQJZtN3O4sIrkYYO3Zr2mHXXlqkPi6MvthptbLNy/dCfVDU28e8c0vHqrYurEHwLgDgR7u3KsomcikVNcw13/2U5MoCcv3DAZl1OcCu669gqEYFA36CFklC2U3dfdhTERfizbbkZKOWB/734/6wkhTMBi4IPWMSllg5SyxPr9diATcLISkX1AUCJ4hXQq9gfKL6EZIpjTAAkx0+yG//7dEbZkl/LHy8cxcljXZp2zJdLfA3MP+kpU1DZx27+3IYA3bkntkePcYBAD9oOyx4SOgkoz1KvTQ3SgJ9UNzZTVNvXzxs6cfhcJ4DwgXUppbh0QQoQIIYzW7xOAEUBWP+3PcQih8iWOtkU4RQV4EOnvwcbMwRUxoTkJeZtBGNucysDqQ4U8vzqDa6dEc1VK37X47EmHuqYWC/e9t4O80lpeujGF2KBTFBMcSoSOVo+Fqn94rDUAYCDXdXJkCOxSYBMwUghhFkLcbp26js4O6znAHmtI7DLgbinl0LiVjp0JFbmqqBvqaD57RDAbM0po7tDiVDNIydsCw8baymEcK6/jpx/sInmYD08s6t7u3xsokajvtvmQlJLHv9jP+oxi/nTFOFsEnsZKa6BB4QEAYoKUSOSW1vbXjs4ah/kkpJTXdzN+SxdjHwMf9/WenJJoq4nBvNVWTG3WiGDe35bHbnMFKbGnUXZBM/BoaQbzdph0AwCNzequvblF8uINk/u84GSEvwd1TS2U1zZ1WQPqzQ05vLcll3vmJnL1lJMX+xuS+EWDi5fq+gdEW8uN5A1gkXAGc5OmPWFjwORh1394ZmIwQsD6I9rkNOgp2AtNNbabhaeXp7Mzt5ynrhxHQkjfdz6L9FflP7qqQbQqvYA//u8AF44J45cXjOzzvQxIDAYITbadJDxcjYT6uHG0RIuEprcwutjV0wEI8HJlXKQf644U9ePGNA4h15pEFzOd5ftO8Nr6bG4+J5ZLx0c45OUj/dWdb0eRSD9Ryf3v7WR0hC/PXjtRh2OfjNBRKjrNSkygZ5+bmzZmFrMxo29uIrVIOCNRKaqeTnNbeYRZw4PZmVdOVf3AjZLQ9IC8LeAbRbN3BL/9fB/jIv145JIe9ofoBSKsJ4n2zuuiqgZufysNb3cTr92Uiqers0TOOymho6GmCGrUh3ZMUN+LxPOrMvjrikN9cm0tEs5IVKpqQnTCVuaK2SNCaLFIXRV2sJO3BaKnsiGzhMKqBu6bl4ibyQGNr6wEerniZjKQbw2DrW9qYck7aZTWNPL6zakM8+u6Gq2mHSHJ6tF6mogJ9OREZT31TS199pL55XW2PuW9jRYJZyQqVT22MzlNjvXHw8XIem1yGryU50FlPsRM59MdZnzdTcxLDnXoFoRQzYeOVdSpZkbL9rAzt5xnr53onD2onRFbGKwSidggT6SkR/knZ4LFIjleXk9kgBaJoYNvBPhG2omEm8nItIRA1mnn9eDFWtSvbtgUvtlfwCXjIxx6imglMsCD/PJ6/rHyCF/uPsavLkrmorHDHL6PAYvPMHD3bwuDDezbCKfi6gYaWyxE6ZPEECNqip1IgPJLZBXXDMruV07Dttfg3auhsh/6AuRtARcvvi4Moq6phcWTIx2/ByDCz4MDxyr4+3dHuColirvPTeiXfQxYhFCnCWsYbEygSjbsq4Q6s/XzQJ8khhpRqVB+FKrbzEtzklQHL21y6kMO/heOrIBX56k2lX3E6+uzuf2tbTQ0t7NT526GqCl8sruA6EAPpvRTTkyEvwdNLZKp8YG9V0RwqNEaBislwd6ueLoayS3txZu7PR/ZHOOt/qPWyLTeRouEs9JakiG/LV9iRKg3Yb5urNUmp76jIg8iJoPBBd5cCHuX9fpLfLrTzB/+e4CV6YU8tzJDDTZUQcE+qkNT2JBZzBUTI/vtw3lecggXjgnjpRtTcDXpj4gzInS0qt9UdRwhRO+GwRYdgk/ugO1vAm3hyvokMdQInwAGk53JSQjBzOHBbMwoxqJbmvY+UkKFGeJmwpLVSiw+vh2+fVy1qeymVMXpsDGzmIeW7WF6QiBXTIrkX2sy2ZdfAYeWg7TwfUMSUsLlk/rH1AQwPsqfl380hcAuMq41PcRWnkM5r6MDPckt7SVzU9Ya9VisOivkl9Xh5+GCd29VBe6ADnh2Vlw9IWxsJ7/EnBEhfLIjn/3HKhkXpaNNepWaImiuV6UVvILhps+p/Pgn+G74O2z4O5XGAAp8xlAVPBFLRAqecVMYFjaMAE+XHt31Hymo4q53thMb5MXLN6qT4oaMYn7x4S6+8nwBQ9AIXsgOZ0K0i0OyqzV9SEg7kRi+gNhAT9YdKZDZ+BEAACAASURBVOqdkuHZHUSiD8NfQYuEcxOVqpoQWVpszWdmDlf9gNceKdIi0dtYiyriZ61JZHLl30E/4+uGcVwZmk9EzQGSyg4xuXw9ZABrIcMSwfcM56jHaIp9x9IUMpph/t6E+3sQ7udOhL8HEf4e1DY2c8ub23AzGXnzllT8PFVp7SevGMfL7/wHg9tOjs/+Ewe/rTlp8x7NAMErCLzD2nIlgjypb7JQVNVAqO9Z5JpYWiDH2n+tJAOkJL+szlZIsC/QIuHMRKXCtleVDTJMxV6H+LiRPMyH7w8Vcu/cRO1U7E0qctWjf1vhug1ZJYjw8dz+k/sAFZNeXFJEZeYWmvPScC/YyQXle/BuWAtFUF/kyj5LHLssiXxsSWSnHI5ZhmAyGHAxGvjgrul2/aPPHx1GaNBqyqq8+UPueEyGKi6b4JgSHJo+JiQZitrMTaCqwZ6VSJzYo3wdUalg3oasLiC/vI5zuukt3htokXBmoqzOa/M2m0iAslc/9XU6v/54L09eMXZg9wl2JjqcJOoaW9hxtJxbZsbZlhgMguCQUIJDLoPpl6lBKZXPIn877vnbmWzeRsqx1YiWr9V1XALI8xyFZfr9JEf5279maTbjq9fzpuFyvjpUyXmjQrUvYLAQOhp2vA0WS7u+ErVMiQs882u2+iOm3AbmbdTkp1Pd0KzNTUOWwATwCFQikXKzbfiuOQnUNjTzz1UZlNQ08tz1k/BwdXzS1aCjIg/cfMFDfZBvyymlscViM/F1ixAQEKu+xi5W0SAtTSoE0pyGR/52krK+h1W3Q+xXqoBjK1teRhhMxF70IHySr8tvDyZCR6mKvhW5RAZEI0Qv9JXIXgvBIyFuNgCV+QeA2D6LbAId3eTcCGFNqkuzHy5K52cjS/n9ojGsTC/gR69voWIAt0d0GirMbf4IlFPZ1WggNe4M8hWMLipCLfV2uPxFuHM1eAbDe9eqUwcos8HOd2DsYhZMncj6X83jgtFhvfTLaPqdduU53ExGIvw8zk4kmhshdxMknKsqMpg8aDyhivr15UlCi4SzE5WqMjfrK6G2FP73C/jXDPj3ZdyU1MLz109mj7mCq1/eyPEeNrDXdEN5np0/Yn1GMZNi/Hun6qlPGNzwETTVq4zuunJlimishun3AhAV4Kl9TIOJEGvPDVsY7FmKRH4aNNVC/BzVtyJoOMYylWejTxJDmagpgITvHofnUiDtdZh8E5jcYMVvuGR8OG/dlsqx8nqufHEjGYVV/b3jgUtFru0kUVrTyIHjlcw6lanpdAhNhuv+AyWZ8MGNsOVliJ0FERN77zU0zoO7r3o/FewHIDbQ6+yaD2WtAQTEzVI/Bw/HqyobdxcDQX3ox9Ii4exEpgAC0t5Q0RJ3rYXL/gGzfwaH/gdZ3zMjMZj3l0ynsUVy1Uub2H60rL93PfCor1TmH+tJYlNmCVLCjN4UCVB3gYueV2GMFXlwzn29e32NcxE1BXLWg5TEBHlSXN1AbWPzmV0re60yYXpYzZ9BI/BvOE6sn6lPT6BaJJwddz9Y+Fe46g249SsYNk6NT78P/GNg+SPQ0szYSD8+uWcG/h4u3PDaZlalF/TvvgcaFa2RTVEAbMgsxtvNxIS+yEWZcB1c+GdIvhSSLur962uch+HnQfUJKNjfrhrsGZiFG2tUAEvCuW1jwSMwYGGid9/eFGqRGAhMvRPGXqkc2a24uMP5f4DC/bDj34BK2Fl2zwxGhPpw59vb+Sgtr582PACxhb/GAMppPT0hsO/Ci8+5F657V9mWNYOXxPnqMXOlTSTOqBps7iawNKmTaCvBIwAY59a3N4T6HTqQGb0IYmfC6ieVIxQI9nZj6ZLpzEgM4pfL9vCv7zORvVBzaNDTepLwjyavtJajJbWnDn3VaE6FbwSEjoGM72wicUbO66w1quhkzDm2oXrfeAASRd+WtdciMZARAi76s4p6WvtX27C3m4nXb07lBxMi+MvydH7/3wO6IOCpKM8Foyt4hbIxU1XZ1SKh6RWGz4fczfibGvBxN52ZSGSvVZGOrl62ofw6EydkABEt5l7cbGccKhJCiDeEEIVCiH3txj4QQuyyfuUIIXa1m3tYCJEhhDgkhLjQkXsdMIRPgEk3wpaXoDjDNuxqMvD3aydy28x43tyQw4Mf7KKx2dKPG3VyKszKH2EwsCGjhBAfN0aE6iJ7ml5g+HnQ0ojI2XBmJcNrS+H4bnt/BKr6a5YlnKD63F7cbGccfZJ4C7Dz1Ekpr5VSTpRSTgQ+Bj4BEEKMBq4Dxlif86IQQqcVd8WC34LJA1Y8ZjdsMAh+c+kofn1xMl/sPsaP39vRTxscAFTkgV80Uko2ZhYzMzFI5yxoeoeYc8DFEzK+IzbIk9zTDYM9ugGQ9v4IVPXXLBmOZ2V2r5Sx7w6HioSUci1Q2tWcUH+R1wBLrUOLgPellA1SymxU3c2pDtnoQMM7FOb8Ag5/DZmr7KaEENx9biJ3zIpnxYEC6ptaurnIEMeaSHeooIri6kZtatL0HiY3VUYjcyXRgZ7kldXS3HIap/qsNUpkWhuRWckvqyObSAwN5VBb0subbsOZfBKzgQIp5RHrz5FA+/Acs3XMDiHEEiFEmhAirahoCLf1nH4PBMTZQmI7Mj5a1SPK6aM+uwOa5gYVpugXw/oj2h+h6QOGnwelWcwKrKKpRbIyvbDnz81eq04jJvuEufzyOso8YtUPxYd7cbP2OJNIXE/bKaLHSClfkVJOkVJOCQkJ6YNtDRBMbnDBH1VpYmtbw/bEBymHV06xFolOVFgdf35R7MorJypA9YDQaHqN4QsAmMEuIvzceXtTTs+eV3kcig918keAOkk0+CWqH4qPdJrvLZxCJIQQJmAx8EG74XygfUnMKOuYpjuSL1XH2tV/gjr7BJu4YBV+l13cS312BxPtwl8LKuv7tFiaZogSmAABcRgzV3HD9Fg2ZJT0rIROa4OhDv4IUCcJt+AYMLpBySAXCeA8IF1K2T6W6wvgOiGEmxAiHhgBbO2X3Q0UhICLnoL6cljztN2Uj7sLwd5uZBdX99PmnJh2fSQKKhsIO5umMBpNVwgBiQsgey3XTg7D1WjgnU1HT/28rDXg7g/DxtsNN7dYOFFZT0SANwQl2kU29jaODoFdCmwCRgohzEKI261T19HB1CSl3A98CBwAlgP3SSm11/VUDBurCgBufQWK7O2UCcFe5OiTRGcq8gCB9I2gsKqeMF+3/t6RZjAy/DxoqiG4dCeXjg9n2XYzVfUnKfEvpepnHTfL1r64lROV9bRYpKr+GjR88JwkpJTXSynDpZQuUsooKeXr1vFbpJQvdbH+SSllopRypJTya0fudUAz7zEVDbHiUbvhuGBPsrRPojPleeATTmWTgfomiz5JaPqG+NlgMEHGd9w0I46axhY+3XkSC3pZtrqBSZjbaSq/TNV/ivT3gOAkKMtRja76AGcxN2l6E+8QOPchOLICjnxnG44P9qa4uuHkdy9DkQoV/lpYWQ+oPuIaTa/j5qOilDJWMjHanwlRfry96Wj3ZXOy16rHbvwRYO0jETwCLM1Qmt0n29YiMViZepdyln3ziO0OI97qvNYmpw5YE+kKKhsA9ElC03ckzIWCfVBbyk3nxJFRWM2mzG5yHLLWgPcwdVLogN1JIkgV+usrk5MWicGKyRUueFKFz6W9AUBcsAqDzda5Em1YLFCRr04SVeokoUVC02eET1CPhQe5ZHw4gV6u/HtTTud1UqqTRPwc++rPVo5V1BHs7Yq7ixGCh6vBPgqD1SIxmBl5sbpzWf0nqC0lzporkV2kRcJG9QlVgrndSSJUm5s0fYWt7/UB3F2MXJsazbcHCli+7zi5JbW0tBbiLDwAtcVd5kcAmMvq2kK13f3AK7TPThK90LxX47QIARf+CV6aBd8/hfvCp4nwc9dZ1+1pH/56vB5vNxNebvrPQtNH+EaAm5+t7/WN02N5b0sud/9H1VVzNRlICPbidpflXA2sqEsiIr+ChBAvu17r+eV1JA/zabtu8Ig+C4PVfw2DnbAxkHIrbHsNptxGfIgX2TrCqY12iXRFVXWE6vBXTV8iBISOUicFlE9h3a/mcaSgiszCGjKKqsksrCYibys5MowlXxQBRba1iaHeJIZ4YS6rY0FyaNt1Z9zfZ0X+tEgMBeY9CnuXwTcPExf4BP/de6K/d+Q8lFvLLPtFU1C5hzAf7Y/Q9DFho2Hfx+pDXQh83V1IiQ0kJTZQzbc0w9OHaB53Od9Mn0NmUTUZhdVkFqmvbdmlNDZbGBXu23bNkRf32Xa1SAwFvIJg/qPw9UNcMGoO79YlUVbTSICX68mfZ06D6kJIXuiYffYHFXmqsbybNwVV9aTEBPT3jjSDndDRUP8GVB4Dv041S+H4LmioxDR8LiOH+TCyvVkJsFgkZbWNBJ7q77eX0I7roULqnRA7i5lH/kokRSdPqju+G969Bl5bAB/c0GdJOk5BhdnWR6KgsoFQHdmk6WtszuuDXc9nr1GPcZ3zI0D1iQnydnNYvxMtEkMFgwEufxGDEDzj8jI5RV0UFys6BB/eBC/PgbwtKvxOWqBmEJdgL88D/xgq65ppbLboyCZN3xM6Sj0W7u96PmuN6ovt7RxVrbVIDCUCYrFc+CfOMR4gYF+7cuItzbDub/CvmZCxCs79NTy4RyXkgTI5DUakbEuk0zkSGkfhGQg+4V2fJJrq227QnATtkxhimFJuYuPXbzPr6PNQdL0a/OxuyN8OY66Ahc+AVzAtFklakYlpMHhFoiQTGqshNJmCSi0SGgfSLsLJDvNWaK7vNj+iP9AniaGGEHwQ/kvqcIf3roaXZ0NpFlz1Blz9FpVGP15bl8XcZ1bz86+PA3Aws+/KEPcrZmvl+ehpFOpEOo0jCR2tzLuWDoWts9eCMEDsjP7ZVxdokRiCBIRG83jL7apyZMJcuHcLjL2Sf32fyTl/Wskf/3eQMB93HrlaHXnX7zxAY/Np9OQdKORtVYlNwSNt5iadJ6FxCKGj1YmhY1G+rDUQMVllUTsJWiSGIAkhXnzWmErxkj1w/fvgE8ahE1U8/U06U+IC+eLHM1l2zwwWTk6k2eSFsbaIf2/M6e9t9z55WyEqBQwGCisb8HE32WW1ajR9RlhrhFM753VDlTL7OpE/ArRIDElaazhl1Hvbiof9Y+VhvFxN/OO6iYyP8retNfmGMdq3nn+uPEJRVUO/7LdPqK9UNuHoaQAUVNZrU5PGcQSPBIS98/roRpAtTuWPAC0SQ5J4azXYHGuuxMHjlXy19wS3zozD37NDgo53GBMCGqhvbuGv36Q7eqt9R/52QEJUKgCFVbptqcaBuHqqUv4F7U4S2WtVv2rrjYuzoEViCBLh74Gr0WCr4fSP747g42bijlkJnRd7heDRUMqtM+P5aLuZPeZyB++2j8jbCgiImgKok4QWCY1DCR1lf5LIXgPRU8HFo//21AVaJIYgRoMgNsiT7OIa9h+rYPn+E9w6Kx4/T5fOi73DoLqA++cPJ8jLld99sb/7TloDCfNWCEkGdz+klBRWNmintcaxhI2B0kyVG1FTAif2QrxzmZpAi8SQJS5YVYP9x3dH8HE3cfus+K4XeodCfTk+JgsPXZjMjtxyVh4c4HkTFguYt6m7NqCironGFguhurifxpGEjlIVDYoPQc46NeZk/gjQIjFkiQ/2Iqu4hhUHCrh9Vjx+Hl2cIkCJBEBNEVdMjsTH3cSKAwO8imzxYaivsIlEW9tSfZLQOJD2NZyy14CrN0RM6t89dYEWiSFKfLAXLRaJr7uJ27o7RYDqeAVQXYiL0cCcpBBWpRdhsQxgk1NrEl1Uq0jobGtNPxCYCEZX5bzOXguxM8HYzc1aP6JFYoiSGOINwB2zE/B1P8kbs91JAmBBcijF1Q3sO1bR11vsO/K2qvLgQao3sE0ktLlJ40iMJhUKm7ESSjKcLj+iFYeJhBDiDSFEoRBiX4fx+4UQ6UKI/UKIp61jcUKIOiHELuvXS47a51BhSmwA/7huIkvmdBHR1J5WkaguAODcpBCEgFXpA9gvkbdVhb4a1Nu/0Jr/oR3XGocTNrotoc4J/RHg2JPEW8BF7QeEEPOARcAEKeUY4Jl205lSyonWr7sdt82hgcEgWDQxEncX48kXtjM3AQR5uzEp2n/gikRdmXIUWk1NAIWV9fi6m079b6HR9DatZcM9g1R5cCfEYSIhpVwLlHYYvgd4SkrZYF0zQD95BjEu7qq+UbtKsPOTQ9ljrqDQWu9oQGHerh6jU21DBZU6kU7TT7QKQ9xs28nW2ejvXSUBs4UQW4QQa4QQqe3m4oUQO63js7u7gBBiiRAiTQiRVlQ0iJvj9CfeIVDTXiTCAPg+fQD+e+dtUVU2I1NsQ4VVOpFO00+EjweDCyRd2N876Zb+FgkTEAhMB34JfChUT77jQIyUchLwM+A9IYRvVxeQUr4ipZwipZwSEuIcnZwGHd5hdieJUeE+hPu5D0yTk3mruntza+sbXFDZoOs2afoHn2Hw4F6YcH1/76Rb+lskzMAnUrEVsADBUsoGKWUJgJRyO5CJOnVo+gOvEDuREEIwLzmUdUeKaGhuOckTnQxLizI3tTM1SSkprKrXva01/YdvuK3QpjPS3yLxGTAPQAiRBLgCxUKIECGE0TqeAIwAsvptl0Md71A7cxPA/JGh1DS2sC27rJ82dQYUpUNjlZ3Tuqy2iaYWqRPpNJpucGQI7FJgEzBSCGEWQtwOvAEkWMNi3wdulqow0BxgjxBiF7AMuFtK2dHprXEU3qEqQ7mpzVE9c3gwbiYDK9ML+nFjp8mhr9Rju65fhbq3tUZzUhzWYUVK2Z3R7cYu1n4MfNy3O9L0GK92CXX+0QB4uBo5JzGIVemF/PbS0QgnPi4D0NIMaW+qTnwBsbbhAt22VKM5Kf1tbtIMBLxVNFN7vwSo7OujJbVkWUuOOzWHl0NlPqTeaTesS3JoNCdHi4Tm1Hhbo8Y6+CXmJasTxuqBEOW07TXwjYIku3xOW7e9EH2S0Gi6RIuE5tR42ZfmaCUqwJORYT7OXzq8OAOyVsOUW1S9nHYUVNbj7+mis601mm7QIqE5Nbb6TZ2T5+Ylh7Itp5TK+iYHb+o0SHtdJSxNvrnTlO5trdGcHC0SmlNjcgN3v07mJoAFo0JptkjWHS7uh431gMYa2PkujF7UJnbt0CU5NJqTo0VC0zOsbUw7MinaHz8Pl7PKvq5paGZLVsnZ7K579i6DhgpIvaPL6aKqBt2RTqM5CVokND3DK7RLc5PJaODcpBC+P1TY80ZEn94NXz5g+/HjHWaufWUzeaW1vbVbhZSw7VVVhiNmeqfpExX1FFTWE+6nRUKj6Q4tEpqe4R3a5UkClMmppKaR3ebynl0rZwMc/sb244kKFYa6ubdPE+Ztqrn81Du6LHvw+//ux2gQXDMlundfV6MZRGiR0PQM71Bbd7qOnJsUgqGnjYhamlW+QtVxqFKiU1rTCMDW7F5Oqk97E9x8Ydw1naZWpxfy1d4T/GTBCGKCPHv3dTWaQYQWCU3P8AqBhkpoqus05e/pSkpsQM9EouoYSGtRwBN7AChpFYmcXhSJlmZVhiP5EnDztpuqa2zhN5/vY3ioN3fOPkVnPo1miKNFQtMzusm6bmVecij7j1XaTEfdUp7X9v3x3UDbSeJoSe2pn99T8jZDfTmMvLjT1D9XHcFcVseTl4/F1aT/BDSak6H/QjQ9w9u+jWlHFlgbEa0+dIrTRHmuejS524lEnNXk02uniUNfg9EVEufbD5+o4tW1WVyVEsW0hKDeeS2NZhCjRULTM1pFootcCYCkMG8i/T1ObXKqsJ4kEufbRKKkuoGZw4PxdjOxNbuXnNeHl0PcLLvmQhaL5LHP9uLjbuKRhaN653U0mkGOFglNz/A6+UlCCMH85FDWHymmvukkjYjKc5XpKioVyo/SVF1KZX0zoT7upMQG9I7zuvgIlGRAkr2p6fvDhWzLKePhi0cR6OV69q+j0QwBtEhoeoaXtchfNyIBMD85lLqmFrac7IO+PBf8oiF8grpczg4AAr1dmRofyOGCapuP4ow59LV6HGlfzG/70TJMBsEPJkac3fU1miGEFglNzzC5gkdAt+YmgHMSg3B3MbDq4EkaEVXkqZ4UVpFoNO8EIMjLlWnxgQBsO1u/xOHlEDYW/GPshvfmVzIizEcX89NoTgMtEpqe49V9Qh2Au4uRmYnBrDpUiGow2AGLBSrM6sPbKxh8IzFYw2ADvVwZF+WHm8lwdian2lLI3dypJLiUkv35FYyN8D3za2s0QxAtEpqe4911aY72zB8VSl5pHRmF1Z0nqwugpVGZmwDCJ+BevA9QJwk3k5FJMf5sORvndcZ3Kg+jQ+jricp6SmoaGRfld+bX1miGIFokND3nJKU5Wpk3Ujm4u4xyao1sajUDhU/AuzobD+ptjuRp8UEcOFZ55qXHD32lTjwRk+2G95orABgToUVCozkdtEhoeo53WLelOVqJ8PdgVLgvK7sSidYciVaRGDYegWS0IRd/z1aRCMQilZP5tGluhIyVkHQhGOzf2vuOVWIQMDpcm5s0mtNBi4Sm53iFQGO16tFwEuYnh7D9aBkVtR1OA60i0c7cBDDVLQ+jQRXgmxQTgMkgzswvkbtRlQ7pIst6f34Fw0O98XDVTmuN5nTQIqHpOafIum5lfnIYLRbJmiMdTh0VeSpCqrWWkm8EVUZ/xpuO2pZ4uBoZH+V3ZiJxaDkY3SBhbqepfccqGKtNTRrNaaNFQtNzWus3ncLkNDHan0AvV1Z3NDmV59mHpQpBpjGBZJltt2xqfBB7zOXUNZ4kKa8jUip/RMJccPWymyqsqqegsoGxkVokNJrTxaEiIYR4QwhRKITY12H8fiFEuhBivxDi6XbjDwshMoQQh4QQFzpyr5ouaD1JFB446TKjQTDX2oiopX0jotZEunYcIJ6Y5hxobrCNTYsPpKlFsjPvNPwSRelQfrRTAh3A/vxKAC0SGs0Z4OiTxFuA3V+xEGIesAiYIKUcAzxjHR8NXAeMsT7nRSGENij3J6FjIHwifPc7qDx+0qXzkkMpq21iV+sHvZTWRDr7BLedTbEYabETnsmxAQCk5ZyGSLRmWSd1Fol9+RUIAaN1joRGc9o4VCSklGuBjsbme4CnpJQN1jWtNopFwPtSygYpZTaQAUx12GY1nTGaYPGr0FQPn92jkuO6YU5SCEaDYOVB639nbSk01dqJRItFsq0+Sv1wfI9t3M/DhcQQL/b0tNMdqCzr8Ang27nkxt78CuKDvfB2M/X8ehqNBnAOn0QSMFsIsUUIsUYIkWodjwTaNR/AbB2zQwixRAiRJoRIKyo6ua1c0wuEJMGFf4Ss1bD15W6X+Xm4MKV9I6Jyq3O6nbmprLaRozKURpO3rSJsKxOi/dmVV9F15nZHaoohbyuMXNjl9P5jldpprdGcIc4gEiYgEJgO/BL4UIguGhJ3g5TyFSnlFCnllJCQkL7ao6Y9U25XZp1vH4eC/d0um58cSvqJKvLL69ol0rWJRGlNIxIDlf6jOonExGh/iqsbONaTJkSHvwFkl6am0ppG8svrGBupTU0azZngDCJhBj6Riq2ABQgG8oH2Xs4o65imvxECfvA8uPvCx3cq81MXLBilHN2r0wvbOtK1MzeVVKtqr43BY6Fgn2o5amVClD8Au/N6YHI6/DX4RNjyLtqz/5jKtNZOa43mzHAGkfgMmAcghEgCXIFi4AvgOiGEmxAiHhgBbO23XWrs8Q6BRS9C4X5Y9YculySGeBMd6GEViVxw9QF3f9u8rST4sLHQXA9lbaGwyeE+uBoNpxaJ5gbIXK2yrLs4gO7N1+U4NJqzwaGePCHEUmAuECyEMAOPA28Ab1jDYhuBm6UyRO8XQnwIHACagfuklKcROK9oamrCbDZTX99LvZOHEO7u7kRFReHi4tL1gqQLIPUO2PQ8DD8PEufZTQshWJAcxvvbcmlxycXoH233QV5ao8Je3cNHq4GiQxA8AgA3k5FREb7sOpVI5KxTWeDd+SPyK4kJ9MTPo5vfQaPRnBSHioSU8vpupm7sZv2TwJNn85pmsxkfHx/i4uI4DVfHkEdKSUlJCWazmfj4+O4Xnv8HyF6rop3u2QiegXbT85JDeWtjDrVF2fiExtnNlVhPEj7RVpEoPgRcapufGOXHR9vNtFikrWxHJw59DS6eED+ny+l9xyoYp01NGs0Z4wzmpj6lvr6eoKAgLRCniRCCoKCgU5/AXD1VWGxNMXz5gMqHaEdqnMp5cK0yd0qkK61pxNfdhIunv/IpFB22m58Q7U9tYwuZRV2UHQdrlvVySJgHLu6dpivqmjhaUssY7bTWaM6YQS8SgBaIM6TH/24RE2H+o3DwC9j1nt2Up6uJJD8Lbi3VdpFNoE4SQd5u6oeQJJU13Y4J0cp/0a3JqWAfVJq7zLKGdk5r7Y/QaM6YISESGgcw4ycQOwu+fghKs+ympvhbTwIdsq1LqxttfSQIHgnFR+wS9OKDvPBxM3XvvD60XD2O6Lpiiy7HodGcPVokHMhnn32GEIL09PQu5+fOnUtaWhoACxcupLxcfTiazWYWLVrEiBEjSExM5IEHHqCxsdFh++4RBiNc8RIII3xyl1046zhvdUdv8e1sbrKJREgSNNVAZVuUs8EgGB/tx+7uMq8PfQWRU8AnrNNUfnkdn+zMJ9Lfo+01NBrNaaNFwoEsXbqUWbNmsXTp0lOu/eqrr/D390dKyeLFi7n88ss5cuQIhw8fprq6mkcffdQBOz5N/KPh0v8D81ZY9zfb8HBXVYOpwBBqt7ykppGg9icJsDqv25gQ5U/68SrqmzoEtlWdgGM7ujQ1fb4rn4v+vpa80lp+c+mos/ylNJqhjRYJB1FdXc369et5/fXXef/99wGoq6vjuuuuY9SoUVxxxRXU1dXZ1sfFk7C5dQAAF3ZJREFUxVFcXMyqVatwd3fn1ltvBcBoNPLss8/yxhtvUFtby1tvvcWiRYuYO3cuI0aM4IknnrBd4z//+Q9Tp05l4sSJ3HXXXbS0qA9ab29vHn30USZMmMD06dMpKDh5S9LTYtxVMP5aWPMXyNsGQKQool66cLi6zblssUjKatufJJLVYxfO62aLZP+xSvvXOfyNekxqazBUUdfET5bu5IH3dzEyzIevH5jNRWPDe+9302iGIEOq4tkTX+7nQMcPm7NkdIQvj1825pTrPv/8cy666CKSkpIICgpi+/btrFmzBk9PTw4ePMiePXuYPHlyp+ft37+flJQUuzFfX19iYmLIyMgAYOvWrezbtw9PT09SU1O55JJL8PLy4oMPPmDDhg24uLhw77338u6773LTTTdRU1PD9OnTefLJJ3nooYd49dVXeeyxx3rnHwRg4V/h6Cb45E64ex1BTQWYZTCZRTWcaz0wVNY30WKRbSLhFawaEnU4SUyMbsu8TrFWhwVUQT+/aAhT//abMkv4+Ye7KKxq4BcXJHH3uYmYjPoeSKM5W4aUSPQnS5cu5YEHHgDguuuuY+nSpWRkZPCTn/wEgPHjxzN+/Pgzuvb5559PUFAQAIsXL2b9+vWYTCa2b99Oaqqql1hXV0doqDL3uLq6cumlKh8hJSWFb7/99qx+t064+8Hil+GtS2D5w7jW5FNgCCWjXShra45EkLdVJIRQJqcOJ4kwX3eG+brb+yWa6lSW9eQf0dBi4f9WHOaVdVnEB3nx8T0zbFFRGo3m7BlSItGTO/6+oLS0lFWrVrF3716EELS0tCCEYNKkSad87ujRo1m2bJndWGVlJbm5uQwfPpwdO3Z0ClUVQiCl5Oabb+bPf/5zp2u6uLjYnmM0Gmlubu605qyJnQGzfgrr/oYQRqo9LiCjsE0kWktyBHq5tT0nJAnS/9fpUhOi/ewjnLLWQHMd5tBzufOFjRw8XskN02J49JJReLoOqbe0RtPn6PP4/7d39tFVVVcC/21CJHwICARRAwKBIIbE0KRYtSiK0mo7YyNYHBwYnDoWWSJaOqv1o9aOYF2zWvthbZHWFqXKLMWKRawWFa3W2godCVg0ypfQEUGiFQgBfNnzxzkveSR5kI/37s17d//Weot3zznvsfe592Wfc/Y++wTAsmXLmD59Otu2bWPr1q1s376dYcOGUV5ezsMPu30FGzZsoKqqqtlnJ06cSG1tLQ8++CAAsViMefPmMXPmTHr06AHAqlWrqKmp4cCBAyxfvpxzzjmHiRMnsmzZMnbtcqm6a2pq2LZtW7PvTysTboKTx4LGqD++gM2JMwmf3K9/YuTRgFFQu8dtzEvgjMF92bqnlo9q3Wf0rd9xOKcHn1tez66P67j/3ypYUFliBsIw0oAZiQBYunQplZWVR5RNnjyZLVu2sG/fPkaPHs1tt93WzPcgIogIjz/+OI8++igjR46kqKiIvLw87rzzzoZ248aNY/LkyZSWljJ58mQqKio4/fTTmT9/PpMmTaK0tJSLLrqI9947+mlyKScnFy77BfQdwienjOODfYca/tA3ziQSjES+d1jsbuKXiGeE3fEP3v/HAT5ct4JVh8bwmREn8fQN5zJxdPMQWMMwUoMNvQJg9erVzcrivoiWiMVi7N27l969XTqJwYMHs2LFiqTtCwoKWL58ebPyqVOnMnXq1Gbl+/Y1juinTJnClClTjip/hxgwAm5YT48334c/reGdXfuoGNqvIbnfEUZiQJH794O3YOg5DcVjCvogAr98eQuHt6/lYd1D37E38ovKCttNbxhpxmYSnZDi4mKuvvrq5NlXM5AR+ccDNORh2rP/ED2PyyEvN+HY8j6DXbK+Js7r3nm5FOb34sXq3fxT3jpUunD256aZgTCMALCZRCck2Y7slpg5cyYzZ85MnzAp4pQTutOta5cG53XN/kP069VkJ3SXLi5VeJMwWIB5FxXxbk0tV2y8CxkwDnr2D0Jsw4g8NpMwAiGnizBsQM8jjET/xMimOC2EwQJcXHISXy3LQ3ZWJU3oZxhG6jEjYQTGiIG92LR7P+Cim/q3lFMpv8hldj3YQnrwap/QL8kBQ4ZhpB4zEkZgFOb3YvuHtdQdjh2Z3C+RhhxOzWcTvPU7OGFYo4PbMIy0Y0bCCIwRA3uhCpt372/ZJwGNYbBNjcSh/e4EvFEXt3iWtWEY6cGMRIC0N1X4zp07ueKKKygsLKS8vJxLLrmE6upqtm7dypgxYwKTv6OMGNgLgHU7PuJQrL7l5aZ+w6FL12Z7Jdi0GmIHocj8EYYRJGYkAqS9qcIrKyuZMGECmzZtYu3atXz3u99NbebWgBg2oCci8NqWGqBJSo44ObnQr/DImYQqVP0PdOvj0n0YhhEYZiQCor2pwlevXk1ubi6zZs1qqDvjjDMYP378Ed9fV1fHVVddRUlJCWPHjm3YwPfGG280pAsvLS3l7bffBpKnEU8nebk5DD6hB3/2RqLFmQQceZRpfT2s/BpsXAFnftUZEcMwAiNa+yR+903YuT613zmoBC6+65jN2psqfMOGDc3SdbTEvffei4iwfv163nzzTSZNmkR1dTULFy5k7ty5XHnllRw6dIhYLMbGjRuTphFPNyMG9uL5N10+qaQnxg0YBW8+BYdqnYFYt9QlCzz/5rTLZxjGkUTLSIRIOlOFA7z88svMmTMHgNNOO41TTz2V6upqzjrrLBYsWMCOHTu47LLLGDlyJM8991zSNOLppjC/J8/7SUJSI5E/CjQGSyph+6tw/q1w7tfNYW0YIRCYkRCRXwJfBHap6hhfdjvwH8Bu3+xmVX1KRIYCG4G49/JVVZ1FR2nFiD8ddCRVeHFxcbNU4W1h2rRpnHnmmaxcuZJLLrmE++6776hpxNNN3HkNCWdJNCUe4rr9VZi0AM6+LgDJDMNoiSB9EouBlkJTfqCqZf71VEL5poTyjhuIEOlIqvALLriAgwcPsmjRooayqqoqXnrppSPajR8/noceegiA6upq3n33XUaNGsXmzZsZPnw4119/PZdeeilVVVWhphGPG4m83C7JU3vnnwYFn4Yv/sAMhGGETGBGQlX/ANQE9f91JlKRKvzZZ5+lsLCQ4uJibrrpJgYNGnRE29mzZ1NfX09JSQlTp05l8eLFdOvWjUceeYQxY8ZQVlbGhg0bmDFjRqhpxAvznZFoMSVHnNw8uPpZqPj3QGQyDCM5oqrB/WduGenJJstNM4GPgTXAPFX90Ld7A6j2dbeq6kvNvtB9xzXANQBDhgwpbzoi3rhxI6NHj065LukkFosxcOBAdu7cGXom2HT0X8X8VZzUpzsr5nw2pd9rGEb7EJG1qlrRUl3YIbA/AwqBMuA94Pu+/D1giKqOBb4GPCwivVv6AlVdpKoVqlqRn58fhMxpJxtThSfy2REDKC3oE7YYhmG0glCjm1S1YUeYiPwceNKXHwQO+vdrRWQTUISbbWQ9bUkVnon88IpjO+wNw+gchDqTEJGTEi4rgQ2+PF9Ecvz74cBIYHN7/58gl9SyCes3wzCCDIFdCkwABojIDuDbwAQRKQMU2Ap81Tc/F/gvETkM1AOzVLVdTu+8vDz27NlD//797SSzNqCq7Nmzh7y8vLBFMQwjRAJ1XKebiooKjSfIi3P48GF27NhBXV1dSFJlLnl5eRQUFGStb8QwDMfRHNdZv+M6NzeXYcOGhS2GYRhGRhJ2dJNhGIbRiTEjYRiGYSTFjIRhGIaRlKxyXIvIbqC1SYgGAB+kUZxsIYr9ZDpHgyjqnIxTVbXF3chZZSTagoisSebNNxqJYj+ZztEgijq3B1tuMgzDMJJiRsIwDMNISpSNxKJjNzGIZj+ZztEgijq3mcj6JAzDMIxjE+WZhGEYhnEMzEgYhmEYSTEjYRiGYSQlq42EiFwgIj3DlsPofNizEQ1E5FMiYmmMO0BWGgkRuVJE1gLnA4fDlqezIiLXiMgdItI9bFmCIorPhr/Pc/37SByqIiLTRGQd8DncmTRGO8mqVOEi0hW4AbgFuFhVXw1ZpE6H/yPRFbga+AZQB/weeClMudJNFJ8NEckD5gGzgR4i8oSqbg1XqvTidb4duAKYpqqvJNSJWjhnm8mqmYSqfgK8Dfwa2CYix4nIZBE5OWTROgUicpw6DgN/BUYD9wFXiUj/cKVLL1F6NuJH/6pqHbBGVU8Bfg7MD1WwAPA67wIeAP4sIt1FZJKIHG8Gon1k/D4JEbkZeE5V/+yvBwIzgH/FjZhfB04EXlDVBSLSRVUjN/0UkW8DJcCTwG/jx8H6kddvgfuBR7Opb6L4bIjI7UA+8LyqPhbXyftfXgeuUdXV2aBrHBG5DnhRVdf76xG4o5DLgEHAW4AAz6jqomzSPRBUNSNfwEnAY8BHwNtN6s4C7gQK/PUY4EOgf9hyh9RXN+KWlCYCS4AfAScl1P8L8AQwPGxZ7dnokN63A08BXwJe8Pe9X0L9HOAP+MFhpr+AU4EXgZ3AqiZ1U4EfAgP99YU4I9knbLkz7ZXJy03/wI18+wIficjXEupeA76jqjsAVHUD8DQuNXCk8EsPY3H98RxwB1CLW58HQFWXAh8D54nIp0XkylCETR2RezZ8BM9ngXmquhz4NnAybgAAgKreA+QAlSIyRES+EIqwqaMGeAgYCdSLyMyEuseBb6rqLn/9N6AKiEyQRqrIWCOhqrXASn95I3CLiBznr+tV9SC4H4+I3AP0pvVnTWQkTSNXvKMuBryPc1QDvAP8BhgtIuUJzR8Efurr8gIQNyW0FK2T7c9GC/e5izo/00YajcIrOINYKiJFCc2/ByzDzSh6BCBuSkjybO8Flvh/FwLXJYS7Hlbnn4gPlG7BLTHuDlDsrCBjjISINJNVVff6h+Vl3LRzoS+v95+5FPgTEAMujz802Yr6eXUL14uAAhEp932zFfgLbs02voZ7B86pO0pV7w9M6A7SVOeE8sg8G9q4vr4SGCIip3mjsR43qzoZwA8KvoULVjhdVR8NQ95UEL/vqnrAFz0BVAPfSawXkRnAGly481f8oMloA53acS0i/wyMUNW7E51N8VGFqqqIdFXVT0TkRNxIqgjnjNyLi4/uqtkf9vcF4Ercj+TXqvqOL89R1ZgfRd8AlKvqVF/3Y2Cdqt4vIv2A41R1Z0gqtJmj6NwF92hk3bMhIp8HrsX98V+uqmt8efw+D8bNGI9T1Zt83ZPAr9Q5sQcDqOr2cDRoO0fRueE+J7Qtxw2IJuAc1juBIcDB+PNhtJ1OOZMQka4i8g3gx8D3RKRMXYRGPLQv/kcgH7/XQ1Xfxy2V7AIWA71UdUcm/RFoKyKSJyILgduApcAwYJaIDANIGDX1wTms+4vILSJSCIwCPvHtajLFQLRC5/psejbEkScii4FbcVFovYCviEj/hCVFcMbv90CxiFzvw5q7AvvBGYdMMBCt1Dl+n/vGl5hUdS2wDuereADntH/DDEQHCcpD3tYXUIlbG78BeLVJXQ7OgCwHTscZu+m4ZZT/DFv2gPtpLjDYvz8NeB4fuQTkAvfgpuKDgGJgAW76fVvYsqdR56x7NvzvIce/PxdYmFAnOH/SL3EO+E8Dv8KNvm8PW/Y06nwvzhgM9WU3Atsz+T53xlfoAiTc9OuBu4Av++vchLotuN2T8esz/I/ghISyCqBv2HoE2E+X++vu/gfTzV+vAj7l35c17Sdf3i1sPYLUOROfjaa/h4Tyy3HO19U4P9LZwDjcDClR5xwgL2w9AtZ5Igkhv/ZK0X0JXQD3Y78R+CMwBbd2PBMf3+zbVAJ/T/L5rmHrEHI/5Se0Gezre7fw+ZywdQhB54x7No71e8Ctt5fglpGuBX4BnJil97m1Omfcfc6kV+i5m1RVReR84FZ1O0H3AZNwUSdLfJvH/Rrr11X1eyJykaqu8s7sT8KUPyha00+4H9JbqvqxuHQTJ6rq//p+yriojhTonHHPxlF0VuABVX0h3lZE1uOWYfb7YA7JsvvcWp0z7j5nEoE6rluK7/Zv1wDjAVT1aVyOnWIRGZXQ/Frgv0VkJz6kT7N0a307+qnY1+cDdSIyB3gGKPBtO30/mc7H1Hl0k/0O4P6Q1gIH1GE6Gykn6OimI3Y7Jtzgd4DjRaTEX7+Ii8g5HkBEynAJyh7DrT0/EIy4odHWfoq3/xIwCxgBfF5VVwQga6ownY+tc29xiQmni0gVMBS4KcNmD1HUOaMJxEiIyGdE5DHgXnEZGXN8eXy56y+4cMxJPrb9b8ApOIcjwB5gtqperqr/F4TMYdCBfhrn65cAE1V1rqr+PWj524Pp3Cady1X1EC6C51pVnaGNaSc6NVHUOVtIu5EQkQk0pnt4C5eB84TENWN1ccxrgELgm/6jB/GpEtTFd69Pt6xh0sF+2uzrf6OqqwMWvd2Yzu3+Pbygqn8MWPR2E0Wds4kgZhKlwGuq+hAu7UMusE8bd0/PF5H7gbW4+PZx4k4Oq8GtMUeFjvTT70OSuaOYzqZztuqcNaQ8LYeIfAaoUdVqf12G2+z0I9wJWRtxo8BncFPI63Abu+JpFXrhQto+SqlgnYwo9pPpbDqTpTpnMymbSYjbHr8St7Hpy/5Go6qvA5/H5X6fraoTcPHQFwL7VXWaqr4Tj3JQ1X3Z/HBEsZ9MZ9OZLNU5CqRyuaknbmQwx78fH69Q1b/gQhXj6ZifB/riDnuJpzqOSihbFPvJdDads1XnrKdDRkJEZojIeSLS20eWLAIeAeqAM8WfHywi3XD57Wf7j04E+vl2GRHT3hGi2E+ms+lMluocNdrskxARwSWLexiXbnkTbtQwV1U/8G3OAb6MO4R9iS8rxp2WNQiX2/06Vd2YIj06HVHsJ9PZdM5WnSONti3HSjwjYxEuhz+4RGL3AL9p0vZGYD5uStndl3UnS85Rtn4ynU3naOgc9VerlptEJEdE7gTuFJHzcGcRxLyRieFSN5/t6+L8HJcDfhWwVUROUdUDqrq5Nf9nJhLFfjKdTeds1dlwHNNI+Ju+FjgBt3X+DtxU8XwRGQcN64m3+1ecL+DWH18HSjRDdsO2lyj2k+lsOmerzkYjrckCWw98XxvXFcfiTgO7DfgZUO5D15YDF4jIUHUnftUBF6rqH9Iieecjiv1kOpvO2aqz4WnNctNa4BHxuVZw8c1DVHUxkCMic/woogCI+YcDVX0iYg9HFPvJdDads1Vnw3NMI6Gqtap6UBuzLl6EOyUK4CpcOt8ncecN/xWapwOOAlHsJ9MZMJ2zUmejkVYfOuRHEQqcCPzWF+8FbgbGAFvia46qmtpcHxlEFPvJdDadyVKdjbZtpqvHJeb6ACj1I4dvAfWq+rI5pRqIYj+ZzqZztuocedq0mU5c4q5X/OtXqnp/ugTLZKLYT6az6WxkJ201EgXAdOBuVT2YNqkynCj2k+lsOhvZScpThRuGYRjZQ9BnXBuGYRgZhBkJwzAMIylmJAzDMIykmJEwDMMwkmJGwjAMw0iKGQnD6AAiEhOR10XkDRFZJyLzfLK7o31mqIhMC0pGw+gIZiQMo2McUNUyVS3G5TS6GHf62tEYCpiRMDIC2ydhGB1ARPapaq+E6+HAa8AA4FRgCe5oT3DHdb4iIq8Co4EtwAPAj4G7gAlAN+BeVb0vMCUM4yiYkTCMDtDUSPiyj3Ant+3F5TWqE5GRwFJVrRCRCcDXVfWLvv01wEBVnS8i3XCpuC9X1S2BKmMYLdDqLLCGYbSZXOAnIlKGO+qzKEm7SbiEeVP8dR9gJG6mYRihYkbCMFKIX26KAbtwvon3gTNw/r+6ZB8D5qjqM4EIaRhtwBzXhpEiRCQfWAj8xJ+n0Ad4z5/aNh2In+y2Fzg+4aPPANeKSK7/niIR6YlhdAJsJmEYHaO7iLyOW1r6BOeovtvX/RR4TERmAE8D+315FRATkXXAYuBHuIinv/oT3XYDXwpKAcM4Gua4NgzDMJJiy02GYRhGUsxIGIZhGEkxI2EYhmEkxYyEYRiGkRQzEoZhGEZSzEgYhmEYSTEjYRiGYSTl/wG12LoM6d3kOAAAAABJRU5ErkJggg==\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    }
  ]
}
