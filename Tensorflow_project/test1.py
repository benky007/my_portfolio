import tflearn
import tensorflow
import json

with open("testing.json") as file:
    json_file = json.load(file)

    tag = []
    ans = []

    for test in json_file:
        for tags in json_file[test]:
            tag.append(tags["tag"])
            ans.append(tags["answer"])

    net = tflearn.input_data(shape=[None, 12])
    net = tflearn.fully_connected(net, 12)
    net = tflearn.fully_connected(net, 12)
    net = tflearn.fully_connected(net, 12, activation="softmax")
    net = tflearn.regression(net)

    model = tflearn.DNN(net)

    model.fit(X_inputs=tag, Y_targets=ans)
    model.predict(tag)
