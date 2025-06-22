#Sample Collection Checklist
#This program provides a step-by-step checklist to ensure good practices during sample collection.
#It demonstrates basic Python concepts: print, input, and for loops.

print("------------------💉🩸 SAMPLE COLLECTION CHECKLIST 🩸💉------------------")
print("The checklist covers preparation, during collection and after collection")
print(73*"-") #Using * instead of so many "-"
print("💉 You are now in the 𝗣𝗥𝗘𝗣𝗔𝗥𝗔𝗧𝗜𝗢𝗡 𝗖𝗛𝗘𝗖𝗞𝗟𝗜𝗦𝗧 💉\n")

#This is the preparation list, where each task is enumerated from 1 to 10
preparation = [
    "1. Confirm patient identification (full name - date of birth)",
    "2. Confirm patient's fasting status (if required)",
    "3. Check the lab order and type of test requested",
    "4. Gather necessary supplies (collection tubes - needles - syringes - labels - cotton balls - bandage tape)",
    "5. Check supplies for expiration date and intact packing",
    "6. Use 70% alcohol hand sanitizer",
    "7. Put on new disposable gloves",
    "8. Arrange supplies neatly on a clean tray or work surface",
    "9. Ensure the patient is comfortable and properly positioned for collection",
    "10. Give a brief, clear explanation of the procedure to the patient",
]

for task in preparation: #For each task in the preparation list...
    input(task +" — Press ENTER to confirm") #After completed the task, the user can press enter to continue
    print ("COMPLETED ✅\n") #A completed message is outputted after pressed enter

print(73*"-")
print("𝗣𝗥𝗘𝗣𝗔𝗥𝗔𝗧𝗜𝗢𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅ | During collection | After collection") #After completing all the tasks above, the program skips to the next section
print("💉 You are now in the 𝗗𝗨𝗥𝗜𝗡𝗚 𝗖𝗢𝗟𝗟𝗘𝗖𝗧𝗜𝗢𝗡 𝗖𝗛𝗘𝗖𝗞𝗟𝗜𝗦𝗧 💉\n")

during = [
    "1. Apply tourniquet and select an appropriate vein",
    "2. Clean the puncture site with antiseptic in a circular motion, allow to dry",
    "3. Fill collection tubes in the correct order of draw",
    "4. Gently invert tubes as needed to mix with additives (do not shake)",
    "5. Release the tourniquet before withdrawing the needle",
    "6. Remove the needle and immediately apply clean cotton or gauze with light pressure",
    "7. Ask the patient to keep pressure on the site until bleeding stops",
    "8. Dispose of needle immediately in the sharps container",
    "9. Ensure the patient is comfortable and properly positioned for collection",
    "10. Secure the puncture site with a bandage or tape",
]
for task in during:
    input(task +" — Press ENTER to confirm")
    print ("COMPLETED ✅\n")

print(73*"-")
print("𝗣𝗥𝗘𝗣𝗔𝗥𝗔𝗧𝗜𝗢𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅ | 𝗗𝗨𝗥𝗜𝗡𝗚 𝗖𝗢𝗟𝗟𝗘𝗖𝗧𝗜𝗢𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅ | After collection\n")
print("💉 You are now in the 𝗔𝗙𝗧𝗘𝗥 𝗖𝗢𝗟𝗟𝗘𝗖𝗧𝗜𝗢𝗡 𝗖𝗛𝗘𝗖𝗞𝗟𝗜𝗦𝗧 💉\n")

after = [
    "1. Label each sample tube immediately in front of the patient (include patient name, date, time, and collector’s initials)",
    "2. Verify labels for accuracy",
    "3. Check the patient’s puncture site for bleeding or bruising",
    "4. Provide aftercare instructions if needed",
    "5. Thank the patient and ensure they are feeling well before leaving",
    "6. Remove gloves and dispose of them properly",
    "7. Wash hands entirely",
    "8. Store the collected samples according to test requirements",
    "9. Document the collection in the patient’s record or laboratory system",
    "10. Transport samples to the processing area promptly",
]
for task in after:
    input(task +" — Press ENTER to confirm")
    print ("COMPLETED ✅\n")

print(73*"-")
print("𝗣𝗥𝗘𝗣𝗔𝗥𝗔𝗧𝗜𝗢𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅ | 𝗗𝗨𝗥𝗜𝗡𝗚 𝗖𝗢𝗟𝗟𝗘𝗖𝗧𝗜𝗢𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅ | 𝗔𝗙𝗧𝗘𝗥 𝗖𝗢𝗟𝗟𝗘𝗖𝗧𝗜𝗢𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅")
print("All steps completed safely. Thank you for using the checklist! 💉💚") #Thanking message is outputted after all the section being completed