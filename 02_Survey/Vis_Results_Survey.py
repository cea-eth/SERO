import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib.ticker as mticker
import Functions_FoIP as intfu
from os.path import realpath, dirname, join

#------ FILES SURVEY ------
# import csv files #

folder_path = dirname(realpath(__file__))
path_dir_fr = join(folder_path, "Results_Survey/Formalisation des processus d'inventaire (Responses) - Form responses 1.csv")
path_dir_en = join(folder_path, "Results_Survey/Formalization of inventory processes (Responses) - Form responses 1.csv")
path_dir_de= join(folder_path, "Results_Survey/Formalisierung von Inventarisierungsprozessen (Responses) - Form responses 1.csv")

res_fr = pd.read_csv(path_dir_fr)
res_eng = pd.read_csv(path_dir_en)
res_de = pd.read_csv(path_dir_de)

# rename columns from de and fr to eng
eng_fr = intfu.dict_rename(res_fr,res_eng)
eng_de = intfu.dict_rename(res_de,res_eng)

res_de = res_de.rename(columns = eng_de)
res_fr = res_fr.rename(columns = eng_fr)

# merge csv files #
res_all = pd.concat([res_fr,res_eng,res_de], axis = 0, ignore_index= True)

# Translate likert-answers to integer 1 to 5
# Note in the list l_de the answer "Stimme nicht zu" has been changed to "Simmte nicht zu" due to a typo in
# the possible answers of the survey

l_de = ["Stimme absolut nicht zu", "Simmte nicht zu", "Stimme weder zu noch dagegen", "Stimme zu","Stimme voll und ganz zu"]
l_fr = ["Pas du tout d'accord", "Pas d'accord", "Ni d'accord ni pas d'accord", "En accord avec", "Tout à fait d'accord"]
l_eng = ["Strongly disagree", "Somewhat disagree", "Neither agree nor disagree", "Somewhat agree", "Strongly agree"]
l_num = list(range(1,6))

# make all strings lower case
for i in range(0,len(l_de)):
    l_de[i] = l_de[i].lower()
    l_fr[i] = l_fr[i].lower()
    l_eng[i] = l_eng[i].lower()

for col in range(0,(len(res_all.columns))):
    for row in range(0,(len(res_all.index))):
        for i in range(0,(len(l_de))):
            res_all.iloc[row,col] = str(res_all.iloc[row,col]).lower()
            if res_all.iloc[row,col] == l_de[i] or res_all.iloc[row,col] == l_fr[i] or res_all.iloc[row,col] == l_eng[i]:
                res_all.iloc[row,col] = float(l_num[i])

# ------ CLEAN & SEPARATE RESULTS ------
# create list with Results on: Building level, Assembly level, Element level
    # partition data in csv - meta-data, general info, building, assembly and element level
    # abbreviations - bd = building; ass = assembly ; el = element, mf = missing factors; rf = remove factors

## To do - create function to search for keywords in questions and sort them accordingly // partition more elegant

#Metadata
res_meta = pd.DataFrame(res_all.iloc[:,0])
res_general = pd.DataFrame(res_all.iloc[:,2:5])

#building
res_bd = intfu.prep_plot_df(res_all,None, None,5,19)
"""res_bd = pd.DataFrame(res_all.iloc[:,5:18])
res_bd_d = dict_rename(res_bd, extract_factor(res_bd))
res_bd = res_bd.rename(columns = res_bd_d)
res_bd = num_column(res_bd)"""
res_bd_ief = pd.DataFrame(res_all.iloc[:,19:21])
"""res_bd_mf = pd.DataFrame(res_all.iloc[:,19])
res_bd_rf = pd.DataFrame(res_all.iloc[:,20])"""

#assembly
res_ass =  intfu.rep_plot_df(res_all,None, None, 21,51)
"""res_ass = pd.DataFrame(res_all.iloc[:,21:50])
res_ass_d = dict_rename(res_ass, extract_factor(res_ass))
res_ass = res_ass.rename(columns = res_ass_d)
res_ass = num_column(res_ass)"""
res_ass_ief = pd.DataFrame(res_all.iloc[:,51:53])
"""res_ass_mf = pd.DataFrame(res_all.iloc[:,51])
res_ass_rf = pd.DataFrame(res_all.iloc[:,52])"""

#element
res_el = intfu.prep_plot_df(res_all, None, None, 53, 97)
"""res_el = pd.DataFrame(res_all.iloc[:,53:96])
res_el_d = dict_rename(res_el, extract_factor(res_el))
res_el = res_el.rename(columns = res_el_d)
res_el = num_column(res_el)"""
res_el_ief =  pd.DataFrame(res_all.iloc[:,97:99])
"""res_el_mf = pd.DataFrame(res_all.iloc[:,97])
res_el_rf = pd.DataFrame(res_all.iloc[:,98])"""

#classification
res_class = pd.DataFrame(res_all.iloc[:,99])

# SORT DF by Mean
res_bd = intfu.sort_by_mean(res_bd)
res_ass = intfu.sort_by_mean(res_ass)
res_el = intfu.sort_by_mean(res_el)

# ------ PLOTS LIKERT ------
# STEPS
    # 1. Plot Boxplots --> to do:
        # * Show average experience and distribution of experience in construction and reuse (important?) + max. exp.
        # * Show number of participants
        # * insert mean
        # * make nicer layout (adjust font, adjust colour etc.)
    # 2. Interpret Boxplots (write in thesis + appendix, highlight findings)

l_plts = [res_bd, res_ass, res_el]

meanpointprops = dict(marker='*', markeredgecolor='black',
                      markerfacecolor='firebrick', markersize=5)
flierprops = dict(marker='.', markerfacecolor='#E6E6E6', markersize=5,
                  linestyle='none')
boxprops = dict( linewidth=1, color= '#274257')

# COLORS for layout [#274257 dark Blue, #9FBED5 light Blue, #5B9CCC Blue, #E6E6E6 light grey, #808080 dark grey]

# BOXPLOTS
"""for i in l_plts:
    data = i

    fig, ax1 = plt.subplots(figsize=(15, 10))

    if i is res_bd:
        fig.canvas.manager.set_window_title('Building Level - Factors ')
    elif i is res_ass:
        fig.canvas.manager.set_window_title('Assembly Level - Factors ')
    elif i is res_el:
        fig.canvas.manager.set_window_title('Element Level - Factors ')

    fig.subplots_adjust(left=0.325, right=0.95, top=0.9, bottom=0.25) ##nochmal nachschauen

    bp = ax1.boxplot(data, notch=False, sym='+', vert=False, whis=1.5, showmeans = True,
                     meanprops=meanpointprops,
                     flierprops=flierprops,
                     boxprops = boxprops)


    ax1.xaxis.grid(True, linestyle='-', which='major', color='lightgrey',
                   alpha=0.5)

    if i is res_bd:
        ax1.set(
            axisbelow=True, # Hide the grid behind plot objects
            title='Likert Results - Building Level',
            xlabel='Likert',
            ylabel='Factors')
    elif i is res_ass:
        ax1.set(
            axisbelow=True, # Hide the grid behind plot objects
            title='Likert Results - Assembly Level',
            xlabel='Likert',
            ylabel='Factors')
    elif i is res_el:
        ax1.set(
            axisbelow=True, # Hide the grid behind plot objects
            title='Likert Results - Element Level',
            xlabel='Likert',
            ylabel='Factors')

    ax1.set_yticklabels(list(data.columns), rotation=0, fontsize=8)

    #Legend /
    fig.text(0.9, 0.15, '*', color='black',
             weight='roman', size='medium')
    fig.text(0.92, 0.15, ' Mean Value', color='black', weight='roman',
             size='x-small')
    plt.show() #manually save"""

# VIOLINPLOTS
boxprops_1 = dict( linewidth=0.01, color= '#ffffff')
meanpointprops_1 = dict(marker='*', markersize=0.01)
flierprops_1 = dict(marker='.', markerfacecolor='#ffffff', markersize=0.01,
                  linestyle='none')
medianprops_1 = dict(linestyle='-.', linewidth=0.01, color='#ffffff')

"""for i in l_plts:
    data = i

    fig, ax1 = plt.subplots()

    if i is res_bd:
        fig.canvas.manager.set_window_title('Building Level - Factors ')
    elif i is res_ass:
        fig.canvas.manager.set_window_title('Assembly Level - Factors ')
    elif i is res_el:
        fig.canvas.manager.set_window_title('Element Level - Factors ')

    fig.subplots_adjust(left=0.325, right=0.95, top=0.9, bottom=0.05)

    bp = ax1.boxplot(data, notch=False, sym='+', vert=False,
                     showcaps = False,
                     boxprops = boxprops_1,
                     meanprops = meanpointprops_1,
                     medianprops = medianprops_1,
                     flierprops = flierprops_1) ## cheat by making color transparent!

    vp = ax1.violinplot(data, vert = False,
                        showmeans = True,
                        showmedians = True,)

    # set style
    vp['cmeans'].set_color('#8C2A37')

    for pc in vp['bodies']:
        pc.set_color('#274257')
        pc.set_facecolor('#9FBED5')

    #Labels on y-axis
    #Bug in violinplots, couldn't plot vertical and had to "make a way around"
    ticks_loc = ax1.get_yticks().tolist()
    ax1.yaxis.set_ticks(ticks_loc)
    ax1.yaxis.set_ticklabels(list(data.columns))

    # set axis grid
    ax1.xaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)

    # set title and axis-label
    if i is res_bd:
        ax1.set(
            axisbelow=True, # Hide the grid behind plot objects
            title='Likert Results - Building Level',
            xlabel='Likert',
            ylabel='Factors')
    elif i is res_ass:
        ax1.set(
            axisbelow=True, # Hide the grid behind plot objects
            title='Likert Results - Assembly Level',
            xlabel='Likert',
            ylabel='Factors')
    elif i is res_el:
        ax1.set(
            axisbelow=True, # Hide the grid behind plot objects
            title='Likert Results - Element Level',
            xlabel='Likert',
            ylabel='Factors')

    #Legend /
    #fig.text(0.9, 0.005, 'red line = Mean Value ', color='#8C2A37', weight='roman', size='medium')
    #fig.text(0.92, 0.015, ' blue line = Median Value', color='#274257', weight='roman', size='medium')

    #plt.show() #manually save"""

# BARPLOTS

rfont = {'fontname':'Roboto Mono'}

"""for i in l_plts:
    mean = []

    for j in i.columns:
        mean.append(i.loc[:,j].mean())
    

    fig, ax1 = plt.subplots(figsize=(15, 10))

    y_pos = np.arange(len(i.columns))

    # Adjust Layout
    fig.subplots_adjust(left=0.325, right=0.95, top=0.9, bottom=0.25)
    ax1.xaxis.grid(True, linestyle='-', which='major', color='#808080',
                       alpha=0.5)

    #Adjust colour
    ax1.spines['bottom'].set_color('#ffffff')
    ax1.spines['top'].set_color('#ffffff')
    ax1.spines['right'].set_color('#ffffff')
    ax1.spines['left'].set_color('#808080')

    bars = ax1.barh(y_pos, mean, align='center', color= '#9FBED5', edgecolor = '#ffffff')
    ax1.set_yticks(y_pos, labels=i.columns, **rfont)
    ax1.set_ylabel('Factors', **rfont, fontsize = '12')
    ax1.bar_label(bars, padding = 3, fmt='{:,.2f}') #
    #ax1.invert_yaxis()  # labels read top-to-bottom
    ax1.set_xlabel('Mean Approval on Likert Scale', **rfont, fontsize = '12')


    if i is res_bd:
        ax1.set_title('Factors Building',**rfont, fontsize = '16')
    elif i is res_ass:
        ax1.set_title('Factors Building Assembly', **rfont, fontsize = '16')
    elif i is res_el:
        ax1.set_title('Factors Building Element',**rfont, fontsize = '16')

    plt.show()"""

# Add mean behind factor and export to csv

filesave_dir = join(folder_path, "/Results_Survey")

intfu.filesave(intfu.meanofdf(res_bd),'Building_means_sep',filesave_dir)
intfu.filesave(intfu.meanofdf(res_ass),'Assembly_means_sep',filesave_dir)
intfu.filesave(intfu.meanofdf(res_el),'Element_means_sep',filesave_dir)

# GENERAL INFORMATION
# The relevant columns were exported and then manually visualized, using excel.

"""intfu.filesave(res_meta,'Metadata',filesave_dir)
intfu.filesave(res_general,'General Information',filesave_dir)"""

# ------ ADD / REMOVE FACTORS ------
# STEPS
    # 1. translate answers to english and check for translation-errors (API Deepl?)
    # 2. check for synonyms + shorten if possible
    # 3. check for dublicates
    # 4. create list with factors which should be added on
        # Building Level
        # Assembly Level
        # Element Level
    # 5. finally, the relevant columns were exported and then manually sorted and visualized, using excel.

"""l_save = [res_bd_ief, res_ass_ief, res_el_ief]
for i in l_save:
    path = filesave_dir
    if i is res_bd_ief:
        intfu.filesave(i,'Building',path)
    elif i is res_ass_ief:
        intfu.filesave(i,'Assembly',path)
    elif i is res_el_ief:
        intfu.filesave(i,'Element',path)"""

# ------ CLASSES ------
# create list with results of Question classification
# finally, the relevant columns were exported and then manually sorted and visualized, using excel.

# STEPS
    # 1. manually separate the classes
    # 2. translate answers to english and check for translation-errors
    # 3. only keep subjects
    # 4. check for synonyms
    # 5. check for dublicates
    # 6. cluster answers according to meaning or similarity

"""intfu.filesave(res_class,'Classes',filesave_dir)"""




