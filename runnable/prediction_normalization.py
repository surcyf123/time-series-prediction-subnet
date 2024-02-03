from matplotlib import pyplot as plt
from scipy.stats import pearsonr, spearmanr, norm, yeojohnson
import numpy as np
from sklearn.preprocessing import MinMaxScaler

from vali_objects.scaling.scaling import Scaling


if __name__ == "__main__":
    results = {0: 0.0072840147288130005, 1: 0.004532402232488705, 2: 0.007286376670232068, 3: 0.004233450626365415, 4: 0.004233450637333288, 5: 0.004233450637333288, 6: 0.004233450637333288, 7: 0.004233450637333288, 8: 0.004233450637333288, 9: 0.004233450637333288, 10: 0.004233450626365413, 11: 0.004233450637333288, 12: 0.004233450637333288, 13: 0.004233450637333288, 14: 0.004233450637333288, 15: 0.004233450636829461, 16: 0.004233450637043947, 17: 0.004233450637333288, 18: 0.004233450637286658, 19: 0.004233450637333288, 20: 0.004233450637333288, 21: 0.004233450636956891, 22: 0.004233450637333288, 23: 0.004233450637333288, 24: 0.004233416275406115, 25: 0.004233450635204033, 26: 0.004233450634798279, 27: 0.004233450637333288, 28: 0.0042334506372579735, 29: 0.004233450635226249, 30: 0.004090911517301803, 31: 0.004233450637186433, 32: 0.004233450637333288, 33: 0.004233450633784508, 34: 0.004233450637333288, 35: 0.004233450637333288, 36: 0.004230677351112441, 37: 0.004233450636646424, 38: 0.004233450634743886, 39: 0.004233450634870705, 40: 0.00423345063723218, 41: 0.004233450636575618, 42: 0.004233450636422071, 43: 0.004233450636575618, 44: 0.004233450636422071, 45: 0.004233450636575618, 46: 0.004233450636575618, 47: 0.004233450636575618, 48: 0.004233450636422071, 49: 0.007231147042288444, 50: 0.004233450637252621, 51: 0.0042104436333255365, 52: 0.004233450626365421, 53: 0.004220051957502776, 54: 0.004233450637017686, 55: 0.004233450636422048, 56: 0.004229411851664025, 57: 0.004233450636575599, 58: 0.004233450636575599, 59: 0.004233450636422076, 60: 0.004233450637333224, 61: 0.004233450637333217, 62: 0.0042334506373331755, 63: 0.0042334506373331755, 64: 0.0042334506373331755, 65: 0.004233450637333146, 66: 0.004233450637333146, 67: 0.004233450637333146, 68: 0.004233450637333135, 69: 0.004233450637333007, 70: 0.004233450637332992, 71: 0.007286460467277688, 72: 0.004233450637332938, 73: 0.004233450637332938, 74: 0.004233450544553555, 75: 0.00423345063733257, 76: 0.004233450521491091, 77: 0.0042334506355075595, 78: 0.0042334506358628204, 79: 0.004233450637333337, 80: 0.004233450637345162, 81: 0.004233450637172396, 82: 0.0042334506372895845, 83: 0.0042334506372895845, 84: 0.00423345063728686, 85: 0.00423345063728686, 86: 0.004233450635830031, 87: 0.004223730871711183, 88: 0.004233450617890596, 89: 0.004233450617890596, 90: 0.004233450614493934, 91: 0.004233450614493934, 92: 0.004233450611628285, 93: 0.004233450611628285, 94: 0.004233450611628285, 95: 0.0042220257227696045, 96: 0.004231363811255814, 97: 0.00423345061446205, 98: 0.004233450597532222, 99: 0.004233450597532222, 100: 0.004233450597532222, 101: 0.00423345059723391, 102: 0.004231417878486963, 103: 0.004233450640397353, 104: 0.004220607007501595, 105: 0.004233450658706135, 106: 0.004233450658951806, 107: 0.00423345062000896, 108: 0.004227470768279825, 109: 0.00421822800766074, 110: 0.00421980570713344, 111: 0.004090911571842699, 112: 0.004233450698166513, 113: 0.004233450579315435, 114: 0.004233450579315435, 115: 0.007286829273476477, 116: 0.006316737522908924, 117: 0.004233398221898697, 118: 0.004233360730232443, 119: 0.004233360730232443, 120: 0.004233360730232443, 121: 0.004233290679909379, 122: 0.0042332171004176525, 123: 0.004233250081447648, 124: 0.004233382080276144, 125: 0.004233382080276144, 126: 0.004233382080276144, 127: 0.004233282753455483, 128: 0.004233333700060205, 129: 0.004233333700060205, 130: 0.004233149295912845, 131: 0.00421835356327274, 132: 0.004233167476870633, 133: 0.004233167476870633, 134: 0.004233268193225901, 135: 0.004233268193225901, 136: 0.0042333047563392545, 137: 0.0042333047563392545, 138: 0.004233315482403695, 139: 0.004218493452911175, 140: 0.004216563358269764, 141: 0.007218097387458072, 142: 0.007240348033435909, 143: 0.00420371840529887, 144: 0.004192244920229675, 145: 0.004192244920229675, 146: 0.00419367597285943, 147: 0.004201155326118716, 148: 0.004201155326118716, 149: 0.004211675672062079, 150: 0.004211675672062079, 151: 0.004211675672062079, 152: 0.00420625908048649, 153: 0.0042016390426161745, 154: 0.0042016390426161745, 155: 0.004191629406215113, 156: 0.004191629406215113, 157: 0.007187885653997894, 158: 0.004177703434675003, 159: 0.004177703434675003, 160: 0.004165486148270156, 161: 0.004164347929006266, 162: 0.004166611817917986, 163: 0.004177338778774599, 164: 0.004177338778774599, 165: 0.004164948901358383, 166: 0.004164948901358383, 167: 0.004146983894713321, 168: 0.004219015214225869, 169: 0.004219015214225869, 170: 0.004201809928734166, 171: 0.007185184716434433, 172: 0.00818854031764217, 173: 0.004220796124396645, 174: 0.004220796124396645, 175: 0.004252573189793801, 176: 0.004273091024639761, 177: 0.0033832860943103756, 178: 0.004075161875283545, 179: 0.0035693534272164397, 180: 0.0033618934926137366, 181: 0.007859774280961965, 182: 0.003668733051292566, 183: 0.0036701811593934843, 184: 0.0033618934926137366, 185: 0.0032002152398658557, 186: 0.0038093841109529698, 187: 0.005039819840255772, 188: 0.005039819840255772, 189: 0.005039819840255772, 190: 0.00334754318554857, 191: 0.0049909516381327545, 192: 0.003836769538710723, 193: 0.0031778286857031845, 194: 0.0042724007943358705, 195: 0.00831922864354045, 196: 0.003525281934585116, 197: 0.0038175143307363087, 198: 0.0029248416249386673, 199: 0.0033003562957823825, 200: 0.003254410506899384, 201: 0.0032223854110252446, 202: 0.0030506271762943417, 203: 0.0030506271762943417, 204: 0.003046225495863424, 205: 0.0035275193209488567, 206: 0.0042613263202739785, 207: 0.002614081261866607, 208: 0.004216508942840261, 209: 0.0026290568927820343, 210: 0.004252988594262543, 211: 0.004252988594262543, 212: 0.004241415300263765, 213: 0.003799472547830937, 214: 0.01877427858149913, 215: 0.004301584384958275, 216: 0.0010086843689178853, 217: 0.003757840122305077, 218: 0.0012597303962332165, 219: 0.0012619109442081249}
    values_list = np.array([v for k, v in results.items()])

    # data with no removals

    # Extracting x and y values
    x_values = [v for k, v in results.items()]
    y_values = [v for k, v in results.items()]

    no_removals_sort = sorted(y_values)

    print("no removals", no_removals_sort)

    # Plotting the graph
    plt.scatter(x_values, Scaling.min_max_scalar_list(y_values), marker='o', label='Data Points')
    plt.title('Scatter Plot of Data')
    plt.xlabel('X-axis (Second Index)')
    plt.ylabel('Y-axis (Third Index)')
    plt.legend()
    plt.grid(True)
    plt.show()

    mean = np.mean(values_list)
    std_dev = np.std(values_list)

    lower_bound = mean - 3 * std_dev
    print("lower bound", lower_bound)
    if lower_bound < 0:
        lower_bound = 0

    filtered_results = [(k, v) for k,v in results.items() if lower_bound <= v]
    filtered_scores = np.array([x[1] for x in filtered_results])

    # Normalize the list using Z-score normalization
    transformed_results = yeojohnson(filtered_scores, lmbda=500)

    plt.hist(transformed_results, bins=1000, density=True, alpha=0.7, color='blue', edgecolor='black')
    # plt.hist(results, bins=1000, density=True, alpha=0.7, color='blue', edgecolor='black')
    plt.show()

    test = []

    for i in range(len(filtered_results)):
        test.append([[filtered_results[i][0], filtered_results[i][1], transformed_results[i]]])

    test_org = sorted(test, key=lambda x: x[0][2])

    # impl with current scoring with removals

    # Extracting x and y values
    x_values = [entry[0][1] for entry in test_org]
    y_values = [entry[0][1] for entry in test_org]

    print("removals", y_values)

    test1 = Scaling.min_max_scalar_list(y_values)

    # Plotting the graph
    plt.scatter(x_values, Scaling.min_max_scalar_list(y_values), marker='o', label='Data Points')
    plt.title('Scatter Plot of Data')
    plt.xlabel('X-axis (Second Index)')
    plt.ylabel('Y-axis (Third Index)')
    plt.legend()
    plt.grid(True)
    plt.show()

    # new impl

    # Extracting x and y values
    x_values = [entry[0][1] for entry in test_org]
    y_values = [entry[0][2] for entry in test_org]

    print("removals distributed", y_values)

    # Plotting the graph
    plt.scatter(x_values, Scaling.min_max_scalar_list(y_values), marker='o', label='Data Points')
    plt.title('Scatter Plot of Data')
    plt.xlabel('X-axis (Second Index)')
    plt.ylabel('Y-axis (Third Index)')
    plt.legend()
    plt.grid(True)
    plt.show()



