from colorama import init
init()
color_dict = {"<b>" : "\033[1;30;40m", #black
           "<r>" : "\033[1;31;40m", #red
           "<g>" : "\033[1;32;40m",#green
           "<y>" : "\033[1;33;40m", #yellow
           "<B>" : "\033[1;34;40m", #blue
           "<p>" : "\033[1;35;40m", #purple
           "<c>" : "\033[1;36;40m",  #cyan
           "<w>" : "\033[1;37;40m"} #white
tag_list = ["<b>","<r>","<g>","<y>","<B>","<p>","<c>","<w>",]
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
            str1 = str1.replace(r, color_dict[r],quantity_similar_tags)
            str1 = str1.replace(r.replace("<","</"),  "\033[1;37;40m",quantity_similar_tags)
   return str1
