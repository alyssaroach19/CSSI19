// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

console.log("script is running...");


const basicAlarm = (alarmMessage)=>{
    return alarmMessage;
;}
console.log(basicAlarm("My alarm!"));


function myAlarm(wakeup){
    console.log("Hey , Alyssa, wakeup!" + wakeup);

}
myAlarm("5pm");


function momAlarm(wakeup)
{
    console.log("Hey, mom, wakeup!" + wakeup);
}
momAlarm("8am");


function familyAlarm(wakeup, now){
    console.log("Hey " + wakeup + " wake up! it's " + now);
}
familyAlarm("alyssa","8am");


function importantAlarm(alarm){
    return alarm.toUpperCase();
}
console.log(importantAlarm("wakeup!"))

function snoozeAlarm(num){
    return "The alarm for "  + num + " has been changed " + (num + 1);
}

// The alarm for 3 has been changed to 4

console.log(snoozeAlarm(6));

var names = ["tanya", "mike", "ken", "tom", "alex", "max"];
var i = 1;
var text = ""

for (names[i]){
    text + names[i] + "wake up" + i++;
}