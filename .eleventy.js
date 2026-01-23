module.exports = function (eleventyConfig){
    eleventyConfig.addPassthroughCopy("./_src/_includes/");
    eleventyConfig.addPassthroughCopy("./_src/css/");
    eleventyConfig.addPassthroughCopy("./_src/img/");
    eleventyConfig.addPassthroughCopy("./_src/js/");

    return{
        dir: {
            input: "_src",
            output: "_site"
        },
    };
};