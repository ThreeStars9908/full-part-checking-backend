# app/api/check_body.py
import cv2
import base64
import numpy as np
from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse
from mmpose.apis import inference_topdown
from pydantic import BaseModel
from model.model import get_model

router = APIRouter()


# Define a Pydantic model for validation
class ImagePayload(BaseModel):
    data: str  # Expecting a base64 string


@router.post("/upload-image/")
async def upload_image(payload: ImagePayload):

    data = payload.data
    
    # Check if the string ends with 'wellz.ai'
    if not data.endswith("wellz.ai"):
        # Return unauthorized response if it doesn't end with 'wellz.ai'
        return JSONResponse({
            "message": "Unauthorized. Invalid data format."
        })
    
    # Remove 'wellz.ai' from the end of the string
    data = data[:-len("wellz.ai")]

    # Load the model
    model = get_model()
    
    # Decode the base64 string into image bytes
    image_data = base64.b64decode(data)

    # Convert the bytes to a numpy array and then decode into an image
    image = cv2.imdecode(np.frombuffer(image_data, np.uint8), cv2.IMREAD_COLOR)
    
    # Perform inference to get keypoints and scores
    result = inference_topdown(model, image)[0].pred_instances
    keypoint_scores = result.keypoint_scores[0]  # Array of scores for each keypoint

    # Return the response
    return JSONResponse({
        "full_body": all(score > 0.5 for score in keypoint_scores),
        "message": "Image processed successfully!",
    })

@router.post("/testapi/")
async def testapi():
    return JSONResponse({
        "message": "successed"
    })