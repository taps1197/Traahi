// replace these values with those generated in your TokBox Account
var apiKey = "46172992";
var sessionId = "2_MX40NjE3Mjk5Mn5-MTUzNDYwMzU3OTc4NH5jNm1CUWJ4YzUxek1jU05hRnpKbDNobXF-fg";
var token = "T1==cGFydG5lcl9pZD00NjE3Mjk5MiZzaWc9YTBlMzFhYTAyMTY4OTNjNjBlZTM1MDQyMzYwY2VlZTFiMzNmZDkxZTpzZXNzaW9uX2lkPTJfTVg0ME5qRTNNams1TW41LU1UVXpORFl3TXpVM09UYzROSDVqTm0xQ1VXSjRZelV4ZWsxalUwNWhSbnBLYkROb2JYRi1mZyZjcmVhdGVfdGltZT0xNTM0NjA2MzM3Jm5vbmNlPTAuMDIyNzYyNTA3OTQxNTgzMTg4JnJvbGU9cHVibGlzaGVyJmV4cGlyZV90aW1lPTE1MzcxOTgzMzImaW5pdGlhbF9sYXlvdXRfY2xhc3NfbGlzdD0=";

// Handling all of our errors here by alerting them
function handleError(error) {
  if (error) {
    alert(error.message);
  }
}

// (optional) add server code here
initializeSession();

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
    // If the connection is successful, initialize a publisher and publish to the session
    if (error) {
      handleError(error);
    } else {
      session.publish(publisher, handleError);
    }
  });
}
