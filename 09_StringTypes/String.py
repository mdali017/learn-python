

# ************** Welcome To String **********
chai = "Lemon";
# print(chai);
chai = "Masala Chai";
first_char = chai[0];
# print(first_char);
# print(chai);


# slice
slice_chai = chai[0:6];
# print(slice_chai);
# print(chai[-1])

num_list = "0123456789";
# print(num_list)
# print(num_list[:])
# print(num_list[3:])
# print(num_list[:4])
# print(num_list[0:7:2])

# print(chai)
# print(chai.lower())
# print(chai.upper())

chai = "    Masala Chai    ";
# print(chai)
# print(chai.strip())

chai = "Lemon";
# print(chai.replace("Lemon", "Ginger"))

chai = "Lemon, Ginger, Masala, Mint";
# print(chai.split())
# print(chai.split(", "))


chai = "Masala Chai";
# print(chai.find("Chai"))
# print(chai.find("chai"))

chai = "Masala Chai Chai Chai";
# print(chai.count("Chai"));

chai_type = "Masala";
quantity = 2;
order = "I ordered {} cups of {} chai";
# print(order);
# print(order.format(quantity, chai_type))

chai_varity = ["Lemon", "Masala", "Ginger"];
# print(chai_varity)
# print(" ".join(chai_varity));
# print(len(chai))

chai = "Masala\nChai";
print(chai)

chai = "Masala chai"
print("Masala" in chai)