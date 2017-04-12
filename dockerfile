FROM gcr.io/tensorflow/tensorflow
RUN apt-get update && apt-get install -y git-core tmux
RUN git clone https://github.com/awjuliani/dfp.git /notebooks/dfp
WORKDIR "/notebooks"
RUN pip install -r ./dfp/requirements.txt
CMD ["/run_jupyter.sh"]