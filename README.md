
1. **Clone the repository**:
    ```bash
    git clone https://github.com/abhi-gowdaa/recipe-backend.git
    cd recipe-backend
    ```

2. **Set up the virtual environment**:
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
        ```bash
        .\venv\Scripts\activate
        ```

4. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Run the application**:
    ```bash
    flask run
    ```
    or
    ```bash
    python app.py
    ```

---

### OpenSearch Setup

1. **Environment variable**:
    - Set the following environment variable:
      ```bash
      OPENSEARCH_INITIAL_ADMIN_PASSWORD
      ```

2. **For mapping**:
    - Use the following command to create the index mapping:
      ```bash
      curl.exe -H "Content-Type: application/x-ndjson" -X PUT "https://localhost:9200/recipe" -ku admin:admin --data-binary "@map.json"
      ```

3. **For uploading data**:
    - Use the following command to upload bulk data:
      ```bash
      curl.exe -H "Content-Type: application/x-ndjson" -X PUT "https://localhost:9200/recipe/_bulk" -ku admin:admin --data-binary "@bulk_recipe.json"
      ```

---

### Notes

- The two JSON files required for the above commands (`map.json` and `bulk_recipe.json`) can be found in the **opensearch json data** folder.
  
- In the above curl commands:
    - `admin:admin` means `username: admin` and `password: admin`.

- OpenSearch runs on port `9200`.
- OpenSearch Dashboard runs on port `5601`.

- The OpenSearch installation instructions are available in the second part of the YouTube video
  https://www.youtube.com/watch?v=Bl4XQYRmawM


---
frontend repository
https://github.com/abhi-gowdaa/food-recipes-frontend

