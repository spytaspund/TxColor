from colorama import init
init()
color_dict1 = {"b" : ["30","40"], #black
           "r" : ["31","41"], #red
           "g" : ["32","42"],#green
           "y" : ["33","43"], #yellow
           "B" : ["34","44"], #blue
           "p" : ["35","45"], #purple
           "c" : ["36","46"],  #cyan
           "w" : ["37","47"]} #white
code_list = []
tag_list = []

for i in color_dict1.keys():
   tag1 = "<" + i + ">"
   code1 = "\033[1;" + color_dict1[i][0] + ";40m"
   tag_list.append(tag1)
   code_list.append(code1)
   for r in color_dict1.keys():
      tag2 = "<" + i + r + ">"
      code2 = '\033[1;' + color_dict1[i][0] + ";" + color_dict1[r][1] + "m"
      code_list.append(code2)
      tag_list.append(tag2)
color_dict2 = dict(zip(tag_list, code_list))

def find(text):
   str1 = text
   tag_in_text = str1.count("<")
   tag_in_text /= 2
   counted_tags = 0
   for i in range(int(tag_in_text)):
      for r in tag_list:
         quantity_similar_tags = str1.count(r)
         c = counted_tags
         counted_tags += quantity_similar_tags
         if c < counted_tags:
            counted_tags = c + 1
            str1 = str1.replace(r, color_dict2[r],quantity_similar_tags)
            str1 = str1.replace(r.replace("<","</"),  "\033[1;37;40m",quantity_similar_tags)
   return str1
