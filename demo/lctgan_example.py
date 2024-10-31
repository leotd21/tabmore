import pandas as pd

from light_ctgan.actgan import ACTGAN


class EpochTracker:
    """
    Simple example that just accumulates ``EpochInfo`` events,
    but demonstrates how you can route epoch information to
    arbitrary callables during model fitting.
    """

    def __init__(self):
        self.epochs = []

    def add(self, epoch_data):
        self.epochs.append(epoch_data)


def main():
    train_df = pd.read_csv("http://gretel-public-website.s3-website-us-west-2.amazonaws.com/datasets/311_call_center_10k.csv")
    print(train_df.head())

    epoch_tracker = EpochTracker()

    model = ACTGAN(
        verbose=True,
        binary_encoder_cutoff=10,
        # use a binary encoder for data transforms if the cardinality of a column is below this value
        auto_transform_datetimes=True,
        epochs=100,
        epoch_callback=epoch_tracker.add
    )

    model.fit(train_df)

    # Tracked and stored epoch information

    # epoch_tracker.epochs[42]
    syn_df = model.sample(100)
    syn_df.head()


if __name__ == '__main__':
    main()
