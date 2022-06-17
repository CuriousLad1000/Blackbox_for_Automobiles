# Event Data Recorder - Black-Box for Automobiles

## Introduction

The problem of road accidents has plagued the world for a very long time. According to the popular statistic published by The World Health Organization, “<i>**Road traffic injuries are the leading cause of death among children and young adults**</i>”. Furthermore, 93% of the world’s 1.3 million road traffic deaths occur in the developing countries. Also, almost 3 to 5% of a country’s GDP is lost annually due to road accidents in the developing countries.

The problem still persists despite an increase in the attempts to changing traffic rules and guidelines. One of the reasons the roads are not safer is due to the lack of accurate data in high detail on the accidents. Getting accurate data will help researchers analyze the causes behind the car accidents, whether due to the machine error or a human error. This will help in making the roads safer and will help in studying the general human behaviour while driving a car to help figure out potential situations where specific habits may lead to an increase in accidents. This will help make the roads safer than ever.

### The solution:

The event data recorder (EDR) as the black box is usually associated with aeroplanes but they are no longer just the key tool in the investigation of aeroplane accidents. By recording the events and actions of the driver including speed, braking, turning, etc. seconds before the collision, the car black box will undoubtedly help the researchers and car manufacturers in making the roads safer. Furthermore, it will benefit both the police and insurance companies to reconstruct and analyze the accident scenario during the investigation.

## Project Objective

The project Black Box was inspired by the real accidental data recorder used in flights. The idea was to implement the same technology in automobiles since there is no such feature or device available for them. Hence, it was decided to make a device which can record data at the time of the crash as it does in flights so that the recorded data can be used to reform the conditions at the time of the crash.

## Basic Hardware used

-   **Micro Computer Board**
-   It acts as the central processing unit.
-   Used to store and process the RAW data received.
-   Acts as the communication medium between sensors.
-   **Accelerometer and Gyroscope**
-   Together used as the steering position measurement unit.
-   **GPS**
-   Used to tell the position of the vehicle.
-   Can also be used to retrieve the moving body’s speed, altitude etc...
-   Can be used to track the vehicle in case of theft.
-   **Wi-Fi**
-   Used to provide the system with high-speed internet access.
-   Cloud backup of Data.
-   **Scanner**
    -   Used to communicate with onboard sensors in the car.

## Software used

-   Custom firmware code built for the embedded computer (Raspberry PI). Written Python.
-   OBD scanner softwares used while developing the project to get debug information.

## Features

-   This product is capable of recording various vehicle parameters which will help police in investigation in case of an accident.
-   The data collected using this device can be used to study accidents in detail and figure out more common causes whether due to machine or human and find an appropriate solution for it.
-   This device will help Insurance companies to filter out any fraud complaints and process legit claims faster providing better services to their customers.
-   This device will particularly be valuable when no witnesses are present at the scene of the accident and each driver has their version of stories.
-   Inbuilt GPS may help user to track their vehicles in case it’s stolen.
-   Real-time monitoring of engine performance.
-   Parents can easily monitor their child’s driving style and habits.
-   Data will be secure even if Black Box is destroyed.

## Planned Future capabilities

-   VOC sensors to detect various indoor conditions and sense the in-car environment.
-   Since the device has internet connectivity, it can support safety features such as remote ignition locking.
-   The Black Box may communicate with the user using an AI-based system to tell them the condition of their vehicle, remind them of the next service date; warn them not to drive rashly etc...
-   A windshield camera can also be integrated to record visual feeds.

#### 

## Device pics

<br/>

**Pics of our prototype built.**

<p align="Center">
  <img src="/osama.tasneem/Blackbox_for_Automobiles/wiki/raw/images/e6bf31870123999e85e8957671828228.jpeg">
</p>


<br/>
<br/>

<br/>

<p align="Center">
  <img src="/osama.tasneem/Blackbox_for_Automobiles/wiki/raw/images/4ba5479e8fb5e85b50eae9bade861670.jpeg">
</p>

<br/>

<p align="Center">
  <img src="/osama.tasneem/Blackbox_for_Automobiles/wiki/raw/images/813f95a2e8c8589f319b5fe85e010c29.jpeg">
</p>

<br/>
<br/>


**Sample Logged Data**

<p align="Center">
  <img src="/osama.tasneem/Blackbox_for_Automobiles/wiki/raw/images/d2fdec2b380311a8cdd6b5741b138162.png">
</p>


<br/>
<br/>

> *For more details, please refer to wiki*
