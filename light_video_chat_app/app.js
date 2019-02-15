// replace these values with those generated in your TokBox Account
var apiKey = "46251422";
var sessionId = "1_MX40NjI1MTQyMn5-MTU0OTk2MzgwMTgwOH4rMFFMK2hHaFBYRm92ZTFwT0laY1JTMk5-UH4";
var token = "T1==cGFydG5lcl9pZD00NjI1MTQyMiZzaWc9M2IwY2RhNjJlNzFmYTI2MDljMWFjOGQ5Yzc2N2I0YmVmMzlhYWE2MTpzZXNzaW9uX2lkPTFfTVg0ME5qSTFNVFF5TW41LU1UVTBPVGsyTXpnd01UZ3dPSDRyTUZGTUsyaEhhRkJZUm05MlpURndUMGxhWTFKVE1rNS1VSDQmY3JlYXRlX3RpbWU9MTU0OTk2MzgxMSZub25jZT0wLjkzMjAzMDk2NTQ2NzkxNiZyb2xlPXB1Ymxpc2hlciZleHBpcmVfdGltZT0xNTUyNTUyMjA3JmluaXRpYWxfbGF5b3V0X2NsYXNzX2xpc3Q9";

initializeSession();
// Handling all of our errors here by alerting them
function handleError(error) {
  if (error) {
    alert(error.message);
  }
}

function initializeSession() {
  var session = OT.initSession(apiKey, sessionId);

  // Subscribe to a newly created stream
session.on('streamCreated', function(event) {
  session.subscribe(event.stream, 'subscriber', {
    insertMode: 'append',
    width: '100%',
    height: '100%'
  }, handleError);
});
  // Create a publisher
  var publisher = OT.initPublisher('publisher', {
    insertMode: 'append',
    width: '100%',
    height: '100%'
  }, handleError);

  // Connect to the session
  session.connect(token, function(error) {
    // If the connection is successful, publish to the session
    if (error) {
      handleError(error);
    } else {
      session.publish(publisher, handleError);
    }
  });
}
