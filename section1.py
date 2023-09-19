from utils import generate_dataframe


def analysis():
    the_data_frame = generate_dataframe()
    summary_stats = the_data_frame.describe()

    # Relationship 1: Body Mass and Bill Length
    avg_body_mass = the_data_frame['body_mass_g'].mean()
    avg_bill_length = the_data_frame['bill_length_mm'].mean()

    # Relationship 2: Species and Bill Depth
    species_bill_depth = the_data_frame.groupby('species')['bill_depth_mm'].mean()

    # Analysis statement
    analysis_paragraph = f"In this penguin dataset, we found that the average body mass of the penguins is approximately {avg_body_mass:.2f} grams, and the average bill length is around {avg_bill_length:.2f} mm. This suggests that there may be a correlation between body mass and bill length, which could indicate that penguins with longer bills tend to have higher body masses. Additionally, when examining the species and bill depth, we observed that Adelie penguins have an average bill depth of {species_bill_depth['Adelie']:.2f} mm. This highlights potential variations in bill characteristics among different species."
    print(analysis_paragraph)

# RUN analysis
analysis()
