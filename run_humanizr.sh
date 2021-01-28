DIR=humanizr/
TWEET_DIR=status_json_all/

./op-classifier/src/twitter-feature-extractor/bin/tfx $DIR/op-classifier/src/twitter-feature-extractor/src/tfx/account_types_testing.conf $TWEET_DIR
./op-classifier/src/ml-classifier/scripts/classifier --model_file resources/model.model  $DIR/op-classifier/src/ml-classifier/src/ml2/libsvm_settings.txt /tmp/organization_personal_testing.json
