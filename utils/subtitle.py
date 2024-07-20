from classextensions.WriteExtension.WriteErrorExt import Writerror
class Subtitles:
    @staticmethod
    def generate_subtitle(chat_now, result_id):
        # Writing to output.txt
        def generate_outputext():
            try:
                with open("output.txt", "w", encoding="utf-8") as outfile:
                    text = result_id
                    words = text.split()
                    lines = [words[i:i + 10] for i in range(0, len(words), 10)]
                    for line in lines:
                        outfile.write(" ".join(line) + "\n")
            except IOError:
                raise Writerror("Error writing to output.txt")
        def generate_chattext():
        # Writing to chat.txt
            try:
                with open("chat.txt", "w", encoding="utf-8") as outfile:
                    words = chat_now.split()
                    lines = [words[i:i + 10] for i in range(0, len(words), 10)]
                    for line in lines:
                        outfile.write(" ".join(line) + "\n")
            except IOError:
                raise Writerror("Error writing to chat.txt")
        generate_outputext()
        generate_chattext()