$(document).ready(function () {

    // Initialize eel
    eel.init()()

    // Animate text elements
    $('.text').textillate({
        loop: true,
        sync: true,
        in: { effect: "bounceIn" },
        out: { effect: "bounceOut" },
    });

    $('.text1').textillate({
        loop: true,
        sync: true,
        in: { effect: 'bounceIn' },
        out: { effect: 'bounceOut' },
        callback: function () {
            $('.text1').addClass('glow-text'); // Add glow effect after animation
        }
    });

    // Siri Waveform animation setup
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 200,
        style: "ios9",
        amplitude: "1",
        speed: "0.30",
        autostart: true,
    });

    // Siri message animation
    $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: { effect: "fadeInUp", sync: true },
        out: { effect: "fadeOutUp", sync: true },
    });

    // Mic button click handler
    $("#MicBtn").click(function () {
        eel.playAssistantSound();
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        eel.allCommands()();
    });

    // Keyboard shortcut: Cmd + J or Ctrl + J to trigger assistant
    function doc_keyUp(e) {
        if (e.key === 'v' && e.metaKey) {
            eel.playAssistantSound();
            $("#Oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            eel.allCommands()();
        }
    }
    document.addEventListener('keyup', doc_keyUp, false);

    // Function to send message from chatbox
    function PlayAssistant(message) {
        if (message != "") {
            $("#Oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            eel.allCommands(message);
            $("#chatbox").val("");
            $("#MicBtn").attr('hidden', false);
            $("#SendBtn").attr('hidden', true);
        }
    }

    // Toggle mic/send buttons based on chatbox input
    function ShowHideButton(message) {
        if (message.length == 0) {
            $("#MicBtn").attr('hidden', false);
            $("#SendBtn").attr('hidden', true);
        } else {
            $("#MicBtn").attr('hidden', true);
            $("#SendBtn").attr('hidden', false);
        }
    }

    // Chatbox keyup event to toggle buttons
    $("#chatbox").keyup(function () {
        let message = $("#chatbox").val();
        ShowHideButton(message);
    });

    // Send button click event
    $("#SendBtn").click(function () {
        let message = $("#chatbox").val();
        PlayAssistant(message);
    });

    // Enter key in chatbox to send message
    $("#chatbox").keypress(function (e) {
        key = e.which;
        if (key == 13) {
            let message = $("#chatbox").val();
            PlayAssistant(message);
        }
    });

    eel.expose(senderText);
    function senderText(text) {
        console.log(">> senderText received:", text);  // ✅ Confirm this logs
        $("#SiriWave").removeAttr("hidden");
        $("#user-command").text("User said: " + text);
    }
    
    eel.expose(DisplayMessage);
    function DisplayMessage(text) {
        console.log(">> DisplayMessage received:", text);  // ✅ Confirm this logs
        $("#SiriWave").removeAttr("hidden");
        $("#status").text(text);
    }
    

    

});
