function setup() {
  noCanvas();

  let lang = navigator.language || 'en-US';
  let speechRec = new p5.SpeechRec(lang, gotSpeech);

  let continuous = true;
  let interim = false;
  speechRec.start(continuous, interim);

  function gotSpeech() {
    if (speechRec.resultValue) {
      createP(speechRec.resultString);
    }
  }
}