#step 1 : setup text to speech -TTS -model (gTTS and Eleven Labs)

import os
from gtts import gTTS

def text_to_speech_with_gtts_old(input_text , output_filepath):
    language = "en"
    
    audioobj = gTTS(
        text = input_text,
        lang  = language,
        slow = False
        
    )
    
    audioobj.save(output_filepath)

input_text = "Hi , this is havilah"  
#text_to_speech_with_gtts_old(input_text = input_text , output_filepath= "gtts_testing.mp3")
 
 
import elevenlabs
from elevenlabs.client import   ElevenLabs
ELEVEN_LABS_API_KEY = os.environ.get("ELEVEN_LABS_API_KEY")

def text_to_speech_with_elevenLabs_old(input_text , output_filepath):
    client =  ElevenLabs(api_key=ELEVEN_LABS_API_KEY)
    audio =client.generate(
        text = input_text ,
        voice = "Aria",
        output_format= "mp3_22050_32",
        model= "eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)
#text_to_speech_with_elevenLabs_old(input_text , output_filepath = "elevenlabs_testing.mp3")
#step2 : Use Model For Text Output to voice

import subprocess
import platform

    
def text_to_speech_with_gtts(input_text , output_filepath):
    language = "en"
    
    audioobj = gTTS(
        text = input_text,
        lang  = language,
        slow = False
        
    )
    
    audioobj.save(output_filepath)
  

    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
            
        elif os_name == "Windows":  # Windows
            subprocess.run(["cmd", "/c", f"start {output_filepath}"], shell=True)  
            
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")
        

input_text = "Hi , this is havilah, autoplaytesting"  
text_to_speech_with_gtts(input_text = input_text , output_filepath= "gtts_autoplay_testing.mp3")

 
def text_to_speech_with_elevenLabs(input_text , output_filepath):
    client =  ElevenLabs(api_key=ELEVEN_LABS_API_KEY)
    audio =client.generate(
        text = input_text ,
        voice = "Aria",
        output_format= "mp3_22050_32",
        model= "eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        
                
        elif os_name == "Windows":  # Windows
             subprocess.run(["cmd", "/c", f"start {output_filepath}"], shell=True)  

        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
            
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")


text_to_speech_with_elevenLabs(input_text , output_filepath = "elevenlabs_autoplay_testing.mp3")
 

    


