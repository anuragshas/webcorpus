## Indian Corpora



This repository contains newspaper datasets and scraping code for several Indian languages



#### Setup

Run the following command to install the dependencies:
```bash
make build
```



#### Usage

* To re-compile the list of news sources, run:

  ```
  python3 main.py fetch-sources
  ```

* To scrape news sources and build raw dataset, run:

  ```bash
  python3 main.py fetch-news
  ```

* To process a raw dataset, run:

  ```bash
  python3 main.py process-news --corpuspath <path> --lang <langcode>
  ```

  

#### Datasets

* Hindi
* Kannada
* Oriya