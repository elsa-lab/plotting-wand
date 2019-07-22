# Download data from Kaggle datasets
#
# References:
# https://www.kaggle.com/datasets?sort=votes&fileType=csv&license=odb
# https://github.com/Kaggle/kaggle-api

DOWNLOAD_DIR=examples/datasets

################################################################################
# Clean
################################################################################

# Remove all existed CSV files
rm -f $DOWNLOAD_DIR/*.csv

################################################################################
# Download
################################################################################

# Medical Cost Personal Datasets
# https://www.kaggle.com/mirichoi0218/insurance
kaggle datasets download -d mirichoi0218/insurance -p $DOWNLOAD_DIR

# Historical Hourly Weather Data 2012-2017 (Download only "temperature.csv")
# https://www.kaggle.com/selfishgene/historical-hourly-weather-data
kaggle datasets download -d selfishgene/historical-hourly-weather-data -f temperature.csv -p $DOWNLOAD_DIR

################################################################################
# Unzip
################################################################################

# Unzip all ZIP files
unzip "$DOWNLOAD_DIR/*.zip" -d "$DOWNLOAD_DIR"

################################################################################
# Remove Zip Files
################################################################################

# Remove all ZIP files
rm -f $DOWNLOAD_DIR/*.zip
