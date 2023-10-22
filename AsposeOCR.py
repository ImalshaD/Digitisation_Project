import requests
receiptOcrEndpoint = 'https://ocr.asprise.com/api/v1/general' # general OCR API endpoint
imageFile = r"Test_Images\Index_Number\IMG_20231019_092513.jpg" # // Modify this to use your own file if necessary
r = requests.post(receiptOcrEndpoint, data = { \
  'api_key': 'TEST',        # Use 'TEST' for testing purpose \
  'recognizer': 'auto',       # can be 'US', 'CA', 'JP', 'SG' or 'auto' \
  'ref_no': 'ocr_python_123', # optional caller provided ref code \
  }, \
  files = {"file": open(imageFile, "rb")})

print(r.json()) 