<template>
<div id="H1R03Xxzd" v-bind:style="{backgroundImage:'url(/static/backgroundSD5.jpg)'}">
  
  <a href="/#/homescreen"> <button class="backButton"> Home</button> </a>
  <button class="Restart" @click="btnRestartClick" v-bind:style="{visibility:restartVisible}">Start Over</button>
  <button class="sendButton" @click="btnSendClick">Send</button>

  <button class="Back" @click="btnBackClick">Back</button>
  <button class="Next" @click="btnNextClick">Next</button>
  <img class="Redo" @click="btnRedoClick" src='/static/redo.png' alt="Redo"/>
  


  <span class="BotChats" v-bind:style="{visibility:botTextVisible, color: botTextColor}">{{botText}}</span>
  <span class="UserChats" v-bind:style="{visibility:userTextVisible}">{{userText}}</span> 
  <span class="textClass">Text: <a id="msgs">{{msgs}}</a></span>

  <img class="BodyPic" src='/static/body.png' alt="Body" usemap="#bodymap"
   v-bind:style="{visibility:imgBodyVisible}" @click="imgBodyClick"/>
  
  <map name="bodymap">
    <area shape="rect" coords="0,300,0, 300">
  </map>


  <button class="btn0" @click="btn0Click">{{btn0Text}}</button>
  <button class="btn1" @click="btn1Click" >{{btn1Text}}</button>
  <button class="btn2" @click="btn2Click">{{btn2Text}}</button>

  <mdc-textfield class="letsTalkTextField" id="msg_input" label="Let's Talk!" v-model="fieldText" type="text" rows="100" cols="100"></mdc-textfield>
</div>
</template>

<script>
export default {
  name: 'chatbot',

  data(){
    return{
      msgs: 0,
      answer: "",

      userText: "",
      botText: "",

      userTexts: [],
      botTexts: [],

      btn0Text: "",
      btn1Text: "",
      btn2Text: "",
      btn0UserText: "",
      btn1UserText: "",
      btn2UserText: "",
      textSymptoms: {},
      fieldText : "",

      userTextVisible: 'hidden',
      botTextVisible: 'hidden',
      imgBodyVisible: 'hidden',
      restartVisible: 'hidden',

      botTextColor: 'black',
    };
  },

  created(){
      var request = {};
      request.question = "start";
      request.answer = "";
      request.textSymptoms = this.textSymptoms;

      const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(request)
      };

      fetch("http://localhost:8000/med/question", requestOptions)
        .then(response => response.json())
        .then(body => this.setScreenText(body))
        .then(() => this.toggleTextColor())
  },
  
  methods: {

    checkBodyDisplay: function() {
        if (this.botText.endsWith('troubling you?')) {
          this.imgBodyVisible = 'visible';
          this.userTextVisible = 'hidden';
        }
        else this.imgBodyVisible = 'hidden';
    },

    setScreenText: function(body) {

      if (body.disease == 'Allergy') {
        this.botText = "Got it! My prediction is that your symptoms are due to you developing seasonal allergies! Would you like a detailed breakdown of other possible diseases?";
        this.btn0Text = "Yes";
        this.btn1Text = "No";
        this.btn2Text = "Cancel";
        return;
      } 

      else if (body.disease == 'Heartburn' || body.question == 'Heartburn') {
        this.botText = "Makes sense! My prediction is that your symptoms are due to heartburn from what you ate! Would you like a detailed breakdown of other possible diseases here?";
        this.btn0Text = "Yes";
        this.btn1Text = "No";
        this.btn2Text = "Cancel";
        return;
      } 

      else if (body.disease != null) this.botText = "Got it! My prediction is that you have the common cold!";
      else this.botText = body.question; 

      this.btn0Text = body.btn0Text;
      this.btn1Text = body.btn1Text;
      this.btn2Text = body.btn2Text;
      this.btn0UserText = body.btn0UserText;
      this.btn1UserText = body.btn1UserText;
      this.btn2UserText = body.btn2UserText;
      this.textSymptoms = body.textSymptoms;

      this.botTextVisible = 'visible';

      this.checkBodyDisplay();
    },

    toggleTextColor: function() {
      this.botTextColor = 'blueviolet';
      setTimeout(() => {
        this.botTextColor = 'black';
        this.userTextVisible = 'hidden';
      }, 1500)
    },

    btnSendClick: function (event) {
        this.msgs += 1;
        this.userText =  this.fieldText;
        this.userTextVisible = 'visible'

        this.botTexts.push(this.botText);
        this.userTexts.push(this.userText);

        
        if (this.userText.startsWith("My symptoms are:")){
            var request = {};
            var dictSymptoms = {};
            var listSymptoms = this.userText.split(": ")[1].split(",") // use list of symptoms given after the colon, then make a list by splitting on commas
            for (symptom in listSymptoms) dictSymptoms[symptom] = "Yes";
            request.textSymptoms = Object.assign({}, this.textSymptoms, dictSymptoms);
            request.message = this.userText;
            request.question = this.botText;


            const requestOptions = {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify(request)
            };

            fetch("http://localhost:8000/med/convo", requestOptions)
              .then(response => response.json())
              .then(body => this.setScreenText(body))
              .then(() => this.toggleTextColor())
              // .then(response => response.json())
              // .then(body => this.botText = "My prediction is that your disease is: " + body.disease)
              //alert('Hello ' + 'name' + '!');  
        }

        else{
            var request = {};
            request.message = this.userText;
            request.textSymptoms = this.textSymptoms;
            request.question = this.botText;

            const requestOptions = {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify(request)
            };


            fetch("http://localhost:8000/med/convo", requestOptions)
              .then(response => response.json())
              .then(body => this.setScreenText(body))
              .then(() => this.toggleTextColor())
        }

        this.fieldText = "";
    },

    btnChoiceClick(btnNumber) {
      this.msgs += 1;
      this.userTextVisible = 'visible';

      this.botTexts.push(this.botText);
      this.userTexts.push(this.userText);

      var request = {};
      if (this.botText.endsWith('troubling you?')) request.question = "Thank you for letting me know. Can you point me to the part of your body that's troubling you?"
      else request.question = this.botText;
      request.answer = this.answer;
      request.textSymptoms = this.textSymptoms;

      const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(request)
      };

    setTimeout(() => {
        fetch("http://localhost:8000/med/question", requestOptions)
          .then(response => response.json())
          .then(body => this.setScreenText(body))
          .then(() => this.toggleTextColor())
      }, 2000)     
    },

    btn0Click: function(event) {
      if (this.botText.endsWith('possible diseases?')) {
         this.botText = "Your most likely disease is: Allergies (46%) \n \n Other possible diseases include: \n Common Cold: (14%) \n Influenza (10%)"
         this.restartVisible = 'visible';
      }

      else if (this.botText.endsWith('diseases here?')) {
        this.botText = "Your most likely disease is: Heartburn (GERD): (55%) \n \n Other possible diseases include: \n Muscle Strain: (10%) \n Heart Attack (Myocardial Infarction): (4%)  "
        this.restartVisible = 'visible';
      }

      else {
        this.userText = this.btn0UserText;
        this.answer = this.btn0Text;
        this.btnChoiceClick();
      }
    },

    btn1Click: function(event) {
      this.userText = this.btn1UserText;
      this.answer = this.btn1Text;
      this.btnChoiceClick();
    },

    btn2Click: function(event) {
      this.userText = this.btn2UserText;
      if(this.btn2Text == 'Unsure') this.answer = this.btn0Text;
      else this.answer = this.btn2Text;
      this.btnChoiceClick();
    },

    imgBodyClick: function(event) {
      var xCoord = event.pageX;
      var yCoord = event.pageY;
      var yHead = 225;
     
      if(yCoord > yHead && yCoord < yHead + 60) {this.answer = 'Head'}
      else if(yCoord > yHead + 65 && yCoord < yHead + 115) {this.answer = 'Chest'}
      else {this.answer = 'Stomach'}

      this.userText = "";
      
      this.btnChoiceClick();
      setTimeout(() => {
        this.imgBodyVisible = 'hidden'
      }, 2000)
    },

    btnBackClick: function(event) {
      this.botTexts.push(this.botText);
      this.userTexts.push(this.userText);

      if(this.msgs > 0) {
        this.msgs--;
        this.userText = this.userTexts[this.msgs];
        this.botText = this.botTexts[this.msgs];
        this.userTextVisible = 'visible';
        this.botTextVisible = 'visible';

      }
    },

    btnNextClick: function(event) {
        if(this.msgs < this.botTexts.length - 1) {
        this.msgs++;
        this.userText = this.userTexts[this.msgs];
        this.botText = this.botTexts[this.msgs];
      }
    },

    btnRedoClick: function(event) {
      this.userText = "";
      this.btn0UserText = "Yes, I do have chest pain"
      this.checkBodyDisplay();
    },

    btnRestartClick: function(event) {this.$router.go(this.$router.currentRoute);}
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
  word-break: break-word;
  display: block;
  white-space: pre-line;
  width: 230px;
  height: 300px;
  top: 90px;
  left: 15px;
}

.UserChats{
  overflow: hidden;
  text-overflow: ellipsis;
  position: absolute;
  width: 200px;
  height: 200px;
  top: 220px;
  left: 150px;
  visibility: hidden;
}


.btn0 {
  overflow: hidden;
  text-overflow: ellipsis;
  position: absolute;
  width: 65px;
  height: 30px;
  top: 500px;
  left: 5px;
  font-size: .7em;
  font-weight: bold;
}

.btn1 {
  overflow: hidden;
  text-overflow: ellipsis;
  position: absolute;
  width: 65px;
  height: 30px;
  top: 500px;
  left: 92px;
  font-size: .7em;
  font-weight: bold;
}

.btn2 {
  overflow: hidden;
  text-overflow: ellipsis;
  position: absolute;
  width: 65px;
  height: 30px;
  top: 500px;
  left: 180px;
  font-size: .7em;
  font-weight: bold;
}

.Back{
  overflow: hidden;
  text-overflow: ellipsis;
  position: absolute;
  width: 55px;
  height: 27px;
  top: 13px;
  left: 150px;
}

.Next{
  overflow: hidden;
  text-overflow: ellipsis;
  position: absolute;
  width: 50px;
  height: 27px;
  top: 13px;
  left: 220px;
}

.Restart{
  overflow: hidden;
  text-overflow: ellipsis;
  position: absolute;
  width: 100px;
  height: 27px;
  top: 450px;
  left: 75px;
}

.Redo{
  overflow: hidden;
  text-overflow: ellipsis;
  position: absolute;
  width: 35px;
  top: 45px;
  left: 200px;
}

.BodyPic{
  position: absolute;
  width: 150px;
  top: 220px;
  left: 200px;
}

</style>
