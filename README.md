# PDS
Probabalistic Disease Surveillance

THIS IS A PRELIMINARY RELEASE OF THE ILI TRACKER SOFTWARE TO TRACK
CASES OF ILI DISEASES IN HOSPITAL ED DATA.

UPDATED FILES AND DATA FILES WILL BE PROVIDED WHEN AVAILABLE.

The following files should be present:

    Patient.py - Individual patient type.
    Data.py - ED data.
    Misc.py - Miscellaneous.
    ILI_Tracker.py - The ILI Tracker algorithm.
    Run_ILI_Tracker.py - Driver for ILI tracker.

Set the following parameters in Run_ILI_Tracker.py:

    diseases - A list of logical names of modeled diseases.
    
    priors - The prior probabilities of the modeled diseases.  Should add to 1.0.
    
    ll_fields - The log-likelihood fields of the .csv file with the data.
    
    data_file - The name of the data file.
    
    equivalent_sample_size - Equivalent sample size for smoothing.
    
    base - Logarithmic base of the log-likelihood fields in the data.
    
    empirical_p_window - Size of window to compute empirical-p values.
    
    min_empirical_p_window - Minimum window to compute empirical-p.
    
    window - Size of moving-average window for graphing.
    
    start - Date to start tracking diseases.
    
    end - Date to end tracking diseases.

The data should be in a .csv file with one line per patient.  The
first (index 0) field should hold the date in YYYYMMDD format. Patient
records should appear in chronological order.  There should be a field
for each of ll_fields with a log-likelihood.

    ADMIT_DATE,log10_flu,log10_rsv,log10_hmpv,log10_parainfluenza,log10_other
    20130601,-10.0329060308,-11.0185611662,-10.2616324760,-11.2581801382,-9.07469311054
    20130601,-13.0291665629,-15.3706085383,-16.1937268446,-15.6780165962,-10.6278225310
    20130602,-13.0577121866,-14.7109602074,-13.6097268266,-14.3259426998,-10.3422741951
    ...

The log-likelihood values for each patient can be computed from training data as follows:

    Compute P(finding|disease) as the fraction of patients with disease that also have finding.
    
    Estimate P(findings|disease) for an individual patient as the product P(finding|disease)
    for those findings that are present in the patient.

See Run_ILI_Tracker.py for an example.

