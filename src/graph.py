import matplotlib.pyplot as plt
import datetime
from random import randint, random
from io import BytesIO

# Returns a fake Egold dataset: one list of datetimes and a list of corresponding values
def generate_data():
    # Generate datetimes at 144 second intervals for 24 hrs
    now_stamp = int(datetime.datetime.now().timestamp())
    dates = [datetime.datetime.fromtimestamp(stamp) for stamp in range(now_stamp, now_stamp + 86401, 144)]

    # Generate values going downhill for each datetime
    values = []
    for i in range(len(dates)):
        # new value starts at the previous value
        value = values[i - 1] if i > 0 else randint(100, 200)

        # add a random decimal value and round to 2 decimal places
        value = round(value + random(), 2)

        # add some variation to the value
        value += randint(-6, 4)

        # amplify the climb or the fall
        if i > 0 and value < values[i - 1]:
            value -= 10
        elif i > 0 and value > values[i - 1]:
            value += 10

        values.append(value)

    return dates, values

# From erwanvivien, generates graph with a new dataset,
# and returns a BytesIO of the image of the plotted graph
def get_graph():
    fig, ax = plt.subplots()
    dates, values = generate_data()
    ax.plot(dates, values)

    ymax = max(values)
    xpos = values.index(ymax)
    xmax = dates[xpos]
    ymin = min(values)
    xpos = values.index(ymin)
    xmin = dates[xpos]

    ax.annotate(f"max: {ymax}", xy=(xmax, ymax), xytext=(xmax, ymax))
    ax.annotate(f"min: {ymin}", xy=(xmin, ymin), xytext=(xmin, ymin))
    plt.xticks(rotation=45, ha="right")
    fig.tight_layout()

    plt.plot()
    buf = BytesIO()
    buf.seek(0)
    plt.savefig(buf, format='png')
    buf.seek(0)
    
    return buf
