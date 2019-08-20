# Changelog

## 1.0.6 (2019-08-20)

* Renamed `reduce_annotations_shifts` to `adjust_annotations_shifts`
* Added `helpers.layout.adjust_annotations_font_sizes` function to adjust annotations font sizes

## 1.0.5 (2019-08-20)

* Changed `reduce_annotations_shifts` adjustments to support both X and Y shift adjustments

## 1.0.4 (2019-08-20)

* Fixed NumPy warning raised when the number of Y values is only 1 in `build_confidence_interval_traces` function

## 1.0.3 (2019-07-29)

* Fixed `apply_columns` argument in `helpers.smoothing.smooth` not working when `None` is specified

## 1.0.2 (2019-07-25)

* Added the confidence interval drawing helper function
* Added the reducing annotation shifts helper function
* Changed the input of the smoothing helper function to accept only dataframe
* Can specify category columns in downsampling function
* Downsampling function now only applies to numeric columns

## 1.0.1 (2019-07-23)

* Fixed Plotly dependency version

## 1.0.0 (2019-07-23)

* Added the initial project
