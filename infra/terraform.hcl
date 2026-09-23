resource "google_bigquery_dataset" "raw" {
    dataset_id = "weather_raw"
    location = "EU"
}

resource "google_bigquery_dataset" "anatlytics" {
    dataset_id = "weather_analytics"
    location = "EU"
}