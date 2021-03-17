<template>
<div id="H1R03Xxzd">
  <a href="/#/homescreen"> <button class="backButton"> Back</button> </a>
  <button class="sendButton" @click="btnSendClick">Send</button>

  <span class="BotChats" v-bind:style="{visibility:botTextVisible, color: botTextColor}">{{botText}}</span>
  <span class="UserChats" v-bind:style="{visibility:userTextVisible}">{{userText}}</span> 
  <span class="textClass">Text: <a id="clicks">{{clicks}}</a></span>

  <button class="alrightButton">Alright</button>
  <button class="mildButton">Mild</button>
  <button class="awfulButton">Awful</button>

  <mdc-textfield class="letsTalkTextField" id="msg_input" label="Let's Talk!" value="" type="text" rows="100" cols="100"></mdc-textfield>

</div>
</template>

<script>
export default {
  name: 'chatbot',

  data(){
    return{
      clicks: 0,
      userText: "",
      botText: "",
      userTextVisible: 'hidden',
      botTextVisible: 'hidden',
      botTextColor: 'black',
    };
  },

  created(){
    const requestOptions = 
    {
      method: "GET"
    };

    fetch("http://localhost:8000/med/intro", requestOptions)
      .then(response => response.json())
      .then(body => {
        this.botText = body['message'];
        this.botTextVisible = 'visible';
      })
  },
  
  methods: {
    btnSendClick: function (event) {
        this.clicks += 1;
        this.userText =  document.getElementById('msg_input').children[0].children[0].value;
        this.userTextVisible = 'visible'
        
        if (this.userText.startsWith("My symptoms are:")){
            var symptomFieldName = 'symptoms';
            var request = {};

            var symptoms = this.userText.split(": ")[1].split(",") // use list of symptoms given after the colon, then make a list by splitting on commas
            console.log(symptoms)
            request[symptomFieldName] = symptoms;

            const requestOptions = {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify(request)
            };

            fetch("http://localhost:8000/med/predict", requestOptions)
              .then(response => response.json())
              .then(body => this.botText = "My prediction is that your disease is: " + body['disease'])
              .then(this.botTextColor = 'blue')
            //alert('Hello ' + 'name' + '!');  
        }

        else{
            var messageFieldName = 'message';
            var request = {};
            request[messageFieldName] = this.userText;

            const requestOptions = {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify(request)
            };

            fetch("http://localhost:8000/med/convo", requestOptions)
              .then(response => response.json())
              .then(body => this.botText = body['message'])
              .then(this.botTextColor = 'blue')
            //alert('Hello ' + 'name' + '!');  
        }

        document.getElementById('msg_input').children[0].children[0].value = "";
        setTimeout(this.userTextDisappear, 1000);
    },

    userTextDisappear: function () {
      this.userTextVisible = 'hidden';
      this.botTextColor = 'black';
    },

    colorChangeBlue: function (event) {
      this.botTextColor = 'blue';
    },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#H1R03Xxzd {
  --mdc-theme-primary: #673ab7;
  --mdc-theme-secondary: #f44336;
  --mdc-theme-background: #ffffff;
  position: relative;
  margin: auto;
  background-color: #ffffff;
  overflow: hidden;
  width: 100%;
  height: 100%;
}

.letsTalkTextField{
  --mdc-theme-primary: rgb(205, 133, 232);
  --mdc-theme-background: rgb(0, 0, 0);
  position: absolute;
  width: 160px;
  height: 36px;
  top: 530px;
  left: 5px;
}

.sendButton {
  overflow: hidden;
  text-overflow: ellipsis;
  position: absolute;
  width: 70px;
  height: 36px;
  top: 559px;
  left: 179px;
}

.backButton {
  overflow: hidden;
  text-overflow: ellipsis;
  position: absolute;
  width: 66px;
  height: 27px;
  top: 13px;
  left: 10px;
}

.textClass {
  overflow: hidden;
  text-overflow: ellipsis;
  position: absolute;
  width: 100px;
  height: 100px;
  top: 610px;
  left: 5px;
}

.BotChats {
  overflow: hidden;
  text-overflow: ellipsis;
  position: absolute;
  width: 200px;
  height: 400px;
  top: 70px;
  left: 15px;
}

.UserChats{
  overflow: hidden;
  text-overflow: ellipsis;
  position: absolute;
  width: 200px;
  height: 200px;
  top: 150px;
  left: 150px;
  visibility: hidden;
}


.alrightButton {
  overflow: hidden;
  text-overflow: ellipsis;
  position: absolute;
  width: 65px;
  height: 30px;
  top: 500px;
  left: 5px;
}

.mildButton {
  overflow: hidden;
  text-overflow: ellipsis;
  position: absolute;
  width: 65px;
  height: 30px;
  top: 500px;
  left: 92px;
}

.awfulButton {
  overflow: hidden;
  text-overflow: ellipsis;
  position: absolute;
  width: 65px;
  height: 30px;
  top: 500px;
  left: 180px;
}

</style>
