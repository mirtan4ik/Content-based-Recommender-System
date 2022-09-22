{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "collapsed_sections": [],
      "name": "appmironova.py",
      "authorship_tag": "ABX9TyNNIXYQRIYuIppT5pYRnA1R",
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
        "<a href=\"https://colab.research.google.com/github/mirtan4ik/Content-based-Recommender-System/blob/master/appmironova_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 356
        },
        "id": "IA3WUoMWr_l_",
        "outputId": "cc32c895-1c6c-4bde-9c00-672f60d7a1ea"
      },
      "outputs": [
        {
          "output_type": "error",
          "ename": "ModuleNotFoundError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-1-878d2f377958>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mimport\u001b[0m \u001b[0mstreamlit\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mst\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mpandas\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mpd\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0mst\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwrite\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"'My app'\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0mdf\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mpd\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mread_csv\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"/content/articles_metadata.csv\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'streamlit'",
            "",
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0;32m\nNOTE: If your import is failing due to a missing package, you can\nmanually install dependencies using either !pip or !apt.\n\nTo view examples of installing some common dependencies, click the\n\"Open Examples\" button below.\n\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n"
          ],
          "errorDetails": {
            "actions": [
              {
                "action": "open_url",
                "actionText": "Open Examples",
                "url": "/notebooks/snippets/importing_libraries.ipynb"
              }
            ]
          }
        }
      ],
      "source": [
        "import time  # to simulate a real time data, time loop\n",
        "\n",
        "import numpy as np  # np mean, np random\n",
        "import pandas as pd  # read csv, df manipulation\n",
        "import plotly.express as px  # interactive charts\n",
        "import streamlit as st  # 🎈 data web app development\n",
        "\n",
        "st.set_page_config(\n",
        "    page_title=\"Real-Time Data Science Dashboard\",\n",
        "    page_icon=\"✅\",\n",
        "    layout=\"wide\",\n",
        ")\n",
        "\n",
        "# read csv from a github repo\n",
        "dataset_url = \"https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv\"\n",
        "\n",
        "# read csv from a URL\n",
        "@st.experimental_memo\n",
        "def get_data() -> pd.DataFrame:\n",
        "    return pd.read_csv(dataset_url)\n",
        "\n",
        "df = get_data()\n",
        "\n",
        "# dashboard title\n",
        "st.title(\"Real-Time / Live Data Science Dashboard\")\n",
        "\n",
        "# top-level filters\n",
        "job_filter = st.selectbox(\"Select the Job\", pd.unique(df[\"job\"]))\n",
        "\n",
        "# creating a single-element container\n",
        "placeholder = st.empty()\n",
        "\n",
        "# dataframe filter\n",
        "df = df[df[\"job\"] == job_filter]\n",
        "\n",
        "# near real-time / live feed simulation\n",
        "for seconds in range(200):\n",
        "\n",
        "    df[\"age_new\"] = df[\"age\"] * np.random.choice(range(1, 5))\n",
        "    df[\"balance_new\"] = df[\"balance\"] * np.random.choice(range(1, 5))\n",
        "\n",
        "    # creating KPIs\n",
        "    avg_age = np.mean(df[\"age_new\"])\n",
        "\n",
        "    count_married = int(\n",
        "        df[(df[\"marital\"] == \"married\")][\"marital\"].count()\n",
        "        + np.random.choice(range(1, 30))\n",
        "    )\n",
        "\n",
        "    balance = np.mean(df[\"balance_new\"])\n",
        "\n",
        "    with placeholder.container():\n",
        "\n",
        "        # create three columns\n",
        "        kpi1, kpi2, kpi3 = st.columns(3)\n",
        "\n",
        "        # fill in those three columns with respective metrics or KPIs\n",
        "        kpi1.metric(\n",
        "            label=\"Age ⏳\",\n",
        "            value=round(avg_age),\n",
        "            delta=round(avg_age) - 10,\n",
        "        )\n",
        "        \n",
        "        kpi2.metric(\n",
        "            label=\"Married Count 💍\",\n",
        "            value=int(count_married),\n",
        "            delta=-10 + count_married,\n",
        "        )\n",
        "        \n",
        "        kpi3.metric(\n",
        "            label=\"A/C Balance ＄\",\n",
        "            value=f\"$ {round(balance,2)} \",\n",
        "            delta=-round(balance / count_married) * 100,\n",
        "        )\n",
        "\n",
        "        # create two columns for charts\n",
        "        fig_col1, fig_col2 = st.columns(2)\n",
        "        with fig_col1:\n",
        "            st.markdown(\"### First Chart\")\n",
        "            fig = px.density_heatmap(\n",
        "                data_frame=df, y=\"age_new\", x=\"marital\"\n",
        "            )\n",
        "            st.write(fig)\n",
        "            \n",
        "        with fig_col2:\n",
        "            st.markdown(\"### Second Chart\")\n",
        "            fig2 = px.histogram(data_frame=df, x=\"age_new\")\n",
        "            st.write(fig2)\n",
        "\n",
        "        st.markdown(\"### Detailed Data View\")\n",
        "        st.dataframe(df)\n",
        "        time.sleep(1)"
      ]
    }
  ]
}