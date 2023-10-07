import re


class ValidateResponse:
    def __init__(self, answers, form):
        self.date_re = re.compile("^\d{4}\-(0[1-9]|1[012])\-(0[1-9]|[12][0-9]|3[01])$")
        self.time_re = re.compile("((1[0-2]|0?[1-9]):([0-5][0-9])([AaPp][Mm]))")
        self.answers = answers
        self.form = form
        self.errors = []

    def is_valid(self):

        for q in self.form.questions:
            answer = list(filter(lambda ans: ans["sr_no"] == q.sr_no, self.answers))

            if not answer:
                self.errors.append("Q{} answer not found".format(q.sr_no))
                continue
            elif len(answer) > 1:
                self.errors.append("Q{} multiple answers provided".format(q.sr_no))
                continue
            answer = answer[0]["answer"]

            if q.type == "text":
                continue
            elif q.type == "date":
                if not self.date_re.match(answer):
                    self.errors.append("Q{} Invalid date format provide iso 8601".format(q.sr_no))
            elif q.type == "time":
                if not self.time_re.match(answer):
                    self.errors.append(
                        "Q{} Invalid time format provide HH:MM AM/PM".format(q.sr_no)
                    )
            elif q.type == "mcq":
                print(answer, " ", q.options)
                if not (answer in q.options):
                    self.errors.append("Q{} Answer should be in options".format(q.sr_no))
            elif q.type == "checkbox":
                selected_options = [i.strip() for i in answer.split(",")]
                print("op :", q.options, "ans", selected_options)
                if not set(selected_options).issubset(set(q.options)):
                    self.errors.append("Q{} Answers should be in options".format(q.sr_no))

        if len(self.errors):
            return False
        return True
