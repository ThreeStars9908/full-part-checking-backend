from mmpose.apis import init_model
from mmpose.utils import register_all_modules


# Initialize a global variable for the model
pose_model = None

# Function to initialize the MMPose model
def load_model():
    global pose_model
    
    # Initialize MMPose model
    register_all_modules()
    pose_model = init_model(
        "model/td-hm_hrnet-w48_8xb32-210e_coco-256x192.py",
        "model/td-hm_hrnet-w48_8xb32-210e_coco-256x192-0e67c616_20220913.pth",
        device="cuda:0",
    )

def get_model():
    return pose_model
