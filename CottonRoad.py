import os
import streamlit as st

def main():
    # Set custom creepy theme and font
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Creepster&display=swap');

        .creepy-title {
            font-family: 'Creepster', cursive;
            font-size: 72px; 
            color: #b30404; /* Laal rang*/
            text-align: center; 
            text-shadow: 2px 5px 4px #000000;
        }

        .not-available {
            font-family: 'Creepster', cursive;
            font-size: 20px;
            color: #b30404; /* Laal rang*/
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<h1 class='creepy-title'>Cotton Road</h1>", unsafe_allow_html=True)
    
   # List of people
    people = [
        {
            "name": "Varshit", 
              
            "details": "A23459230**", 
            "ordered": False,
            "organs": [
                {"name": "Heart", "price": "$10,000", "ordered": False},
                {"name": "Eyes", "price": "$5,000", "ordered": True},
                {"name": "Kidneys", "price": "$7,000", "ordered": False}
            ]
        },
        {
            "name": "Aniruddha", 
            
            "details": "A2345923085", 
            "ordered": False,
            "organs": [
                {"name": "Liver", "price": "$8,000", "ordered": False},
                {"name": "Lungs", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Varun", 
              
            "details": "A2345923088", 
            "ordered": False,
            "organs": [
                {"name": "Brain", "price": "$12,000", "ordered": True}
            ]
        },
        {
            "name": "Shreya Singh", 
              
            "details": "Details of Shreya Singh", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$10,000", "ordered": False},
                {"name": "Liver", "price": "$5,000", "ordered": False}
            ]
        },
        {
            "name": "Saurav Kumar", 
              
            "details": "Details of Saurav Kumar", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Siddharth", 
              
            "details": "Details of Siddharth", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Harsh Bansal", 
              
            "details": "Details of Harsh", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Ishika Vashisht", 
              
            "details": "Details of Ishika Vashisht", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        # Add new people
        {
            "name": "Aditya Mavai", 
              
            "details": "Details of Aditya Mavai", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Prakhar Chandra", 
              
            "details": "Details of Prakhar Chandra", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Archi Awana", 
              
            "details": "Details of Archi Awana", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Sumit Bhati", 
              
            "details": "Details of Sumit Bhati", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Daksh Gupta", 
              
            "details": "Details of Daksh Gupta", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
            {
            "name": "Sneha Dawar", 
              
            "details": "Details of Sneha Dawar", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Shashwat Raj", 
              
            "details": "Details of Shashwat Raj", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Athar Qureshi", 
              
            "details": "Details of Athar Qureshi", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        # Add more people here...
        {
            "name": "Ankush Kumar Chhonker", 
              
            "details": "Details of Ankush Kumar Chhonker", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Sandeep Raj", 
              
            "details": "Details of Sandeep Raj", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Mohammad Ashran Khan", 
              
            "details": "Details of Mohammad Ashran Khan", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Chetan Chauhan", 
              
            "details": "Details of Chetan Chauhan", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Nancy Sherawat", 
              
            "details": "Details of Nancy Sherawat", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Amit Kumar", 
              
            "details": "Details of Amit Kumar", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Bhavya Mansharamani", 
              
            "details": "Details of Bhavya Mansharamani", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Devansh Gaur", 
              
            "details": "Details of Devansh Gaur", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Sujal Srivastava", 
              
            "details": "Details of Sujal Srivastava", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Kunal Pratap Singh", 
              
            "details": "Details of Kunal Pratap Singh", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Harsh Srivastava", 
              
            "details": "Details of Harsh Srivastava", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Aarnav Goyal", 
              
            "details": "Details of Aarnav Goyal", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": " Shubham", 
              
            "details": "Details of  Shubham", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Rahul", 
              
            "details": "Details of Rahul", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Adarsh Kumar", 
              
            "details": "Details of Adarsh Kumar", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Radha Krishna", 
              
            "details": "Details of Radha Krishna", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Faizan Ahmad", 
              
            "details": "Details of Faizan Ahmad", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Raghav Naithani", 
              
            "details": "Details of Raghav Naithani", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Anshul", 
              
            "details": "Details of Anshul", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Riyanshi Tyagi", 
              
            "details": "Details of Riyanshi Tyagi", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Niranjan Kumar", 
              
            "details": "Details of Niranjan Kumar", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Meet Patel", 
              
            "details": "Details of Meet Patel", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Samar Ahmad", 
              
            "details": "Details of Samar Ahmad", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },#MADE BY ISHIKA VASHISHT
        {
            "name": "Ritik Singh", 
              
            "details": "Details of Ritik Singh", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Swati Sootha", 
              
            "details": "Details of Swati Sootha", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Aklavya Raj", 
              
            "details": "Details of Aklavya Raj", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Saurav Kumar", 
              
            "details": "Details of Saurav Kumar", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Aman Singh", 
              
            "details": "Details of Aman Singh", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Aman Pal", 
              
            "details": "Details of Aman Pal", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Saransh Srivastava", 
              
            "details": "Details of Saransh Srivastava", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Shreya Singh", 
              
            "details": "Details of Shreya Singh", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Aman Jaiswal", 
              
            "details": "Details of Aman Jaiswal", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Nikhil Narwat", 
              
            "details": "Details of Nikhil Narwat", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Gaurav", 
              
            "details": "Details of Gaurav", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Siddharth Gupta", 
              
            "details": "Details of Siddharth Gupta", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Nitin Gupta", 
              
            "details": "Details of Nitin Gupta", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Raghav Goel", 
              
            "details": "Details of Raghav Goel", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Mrityunjay Singh", 
              
            "details": "Details of Mrityunjay Singh", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Pratyush Verma", 
              
            "details": "Details of Pratyush Verma", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Ayush Pratap Singh", 
              
            "details": "Details of Ayush Pratap Singh", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Syed Abbas Hasan", 
              
            "details": "Details of Syed Abbas Hasan", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
        {
            "name": "Yuvraj Singh Chauhan", 
              
            "details": "Details of Yuvraj Singh Chauhan", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$8,000", "ordered": False},
                {"name": "Liver", "price": "$6,000", "ordered": False}
            ]
        },
         {
            "name": "Dr. Swadha Bhartia", 
              
            "details": "A Professor at Amity University, Noida", 
            "ordered": False,
            "organs": [
                {"name": "Kidney ", "price": "$60,000", "ordered": False},
                {"name": "Liver", "price": "$20,000", "ordered": False}
            ]
        }
]
    # Base URL of the GitHub repository where images are stored
    base_github_url = "https://raw.githubusercontent.com/QuintessenceCoding/cotton-road-images/main/images/"

    # Generate photo paths for each person using the base GitHub URL
    for person in people:
        photo_name = person["name"].replace(" ", "_").lower() + ".jpg"  # Assuming images are in JPG format
        person["photo_path"] = base_github_url + photo_name + "?v=1"

    # Search input
    search_input = st.text_input("Search by name:")
    
    # Filter people 
    filtered_people = [person for person in people if search_input.lower() in person['name'].lower()]

    # Display list of filtered people
    for person in filtered_people:
        st.header(person['name'])
        if all([organ['ordered'] for organ in person['organs']]):
            st.markdown("<p class='not-available'>Not available</p>", unsafe_allow_html=True)
        else:
            st.subheader("Organs for Sale:")
            all_organs_sold = True
            for organ in person['organs']:
                if not organ['ordered']:
                    all_organs_sold = False
                    if st.button(f"Buy {organ['name']} for {organ['price']}", key=f"{person['name']}_{organ['name']}"):
                        st.success(f"You've purchased {organ['name']} from {person['name']}!")
                        st.success("Our dealers will contact you soon, stay tuned!")  # Add message
                  
                        organ['ordered'] = True
                else:
                    st.write(f"{organ['name']} - {organ['price']} (Sold)")
        
            # Option to buy organs in pack
            if not all_organs_sold:
                if st.button(f"Buy all organs in pack", key=f"{person['name']}_pack"):
                    total_price = sum([int(organ['price'].replace("$", "").replace(",", "")) for organ in person['organs'] if not organ['ordered']])
                    st.success(f"You've purchased all available organs from {person['name']} for ${total_price}!")
                    st.success("Our dealers will contact you soon, stay tuned!")  # Add message
                  
                    for organ in person['organs']:
                        if not organ['ordered']:
                            organ['ordered'] = True
        
        # Check if photo_path exists and display image if it does
        if person['photo_path'] and st.image(person['photo_path'], caption=person['name'], use_column_width=True):
            st.image(person['photo_path'], caption=person['name'], use_column_width=True)
        else:
            st.warning(f"No image found for {person['name']}")

        st.write(person['details'])

if __name__ == "__main__":
    main()
