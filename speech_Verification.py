
from speechbrain.pretrained import SpeakerRecognition



def Speaker_Recognition(v1="C:/Users/Asus/Desktop/Untitled Folder/audio-dataset/Actor_01/03-01-01-01-01-01-01.wav" , v2="C:/Users/Asus/Desktop/Untitled Folder/audio-dataset/Actor_01/03-01-01-01-01-01-01.wav" ) :
    verification = SpeakerRecognition.from_hparams(source="speechbrain/spkrec-ecapa-voxceleb", savedir="pretrained_models/spkrec-ecapa-voxceleb")
    score, prediction = verification.verify_files(v1, v2)
    return score , prediction