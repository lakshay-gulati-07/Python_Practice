import requests
import base64
import json

def encode_file_to_base64(file_path):
    """Converts a file to base64 encoding."""
    with open(file_path, "rb") as file:
        return base64.b64encode(file.read()).decode("utf-8")

def analyze_document(file_path):
    """Sends a document to Azure Document Intelligence for analysis."""
    ENDPOINT = "https://<your-region>.cognitiveservices.azure.com/"
    API_KEY = "<your-api-key>"
    MODEL_ID = "<your-custom-model-id>"
    
    url = f"{ENDPOINT}/formrecognizer/documentModels/{MODEL_ID}:analyze?api-version=2023-07-31"
    headers = {
        "Content-Type": "application/json",
        "Ocp-Apim-Subscription-Key": API_KEY
    }
    
    # Convert file to Base64
    base64_content = encode_file_to_base64(file_path)
    payload = {
        "base64Source": base64_content
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 202:
        # Get the operation-location to retrieve results later
        operation_url = response.headers["operation-location"]
        print("Document submitted for processing. Fetching results...")
        return get_results(operation_url, headers)
    else:
        print("Error:", response.text)
        return None

def get_results(operation_url, headers):
    """Retrieves document processing results from Azure."""
    import time
    while True:
        result_response = requests.get(operation_url, headers=headers)
        result_json = result_response.json()
        if result_json.get("status") in ["succeeded", "failed"]:
            return result_json
        print("Waiting for results...")
        time.sleep(5)

def main():
    file_path = input("Enter the file path: ")
    results = analyze_document(file_path)
    if results:
        print("\nExtracted Data:")
        print(json.dumps(results, indent=4))

if __name__ == "__main__":
    main()
